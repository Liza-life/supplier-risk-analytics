import pandas as pd
import numpy as np

np.random.seed(42)

# =========================
# CONFIGURAÇÕES
# =========================
MESES_HISTORICO = 12
DATA_FIM = pd.Timestamp.today().normalize()
DATAS = pd.date_range(end=DATA_FIM, periods=MESES_HISTORICO, freq="MS")

# =========================
# CARREGAR DADOS TRUSTED
# =========================
entregas = pd.read_csv("data/trusted/entregas.csv")
reclamacoes = pd.read_csv("data/trusted/consumidor_gov.csv")

# =========================
# MÉTRICAS BASE POR FORNECEDOR
# =========================
metricas_entrega = (
    entregas
    .groupby("supplier_id")
    .agg(
        atraso_medio=("atraso_dias", "mean"),
        pedidos_incompletos=("pedido_completo", lambda x: (~x).sum())
    )
    .reset_index()
)

reclamacoes["reclamacao_aberta"] = reclamacoes["status_reclamacao"].apply(
    lambda x: 1 if x == "Não Resolvida" else 0
)

metricas_reclamacao = (
    reclamacoes
    .groupby("cnpj")
    .agg(
        perc_reclamacoes_abertas=("reclamacao_aberta", "mean")
    )
    .reset_index()
    .rename(columns={"cnpj": "supplier_id"})
)

base = metricas_entrega.merge(
    metricas_reclamacao,
    on="supplier_id",
    how="left"
).fillna(0)

# =========================
# PERFIL DE COMPORTAMENTO
# =========================
base["perfil"] = np.random.choice(
    ["estavel", "melhoria", "piora", "critico"],
    size=len(base),
    p=[0.4, 0.25, 0.25, 0.10]
)

# =========================
# GERAR SCORE HISTÓRICO
# =========================
historico = []

for _, row in base.iterrows():
    score_base = (
        100
        - row["atraso_medio"] * 2
        - row["perc_reclamacoes_abertas"] * 30
        - row["pedidos_incompletos"] * 1
    )

    score_base = np.clip(score_base, 40, 95)

    tendencia = {
        "estavel": 0,
        "melhoria": 1.5,
        "piora": -1.5,
        "critico": -3
    }[row["perfil"]]

    score_atual = score_base

    for data in DATAS:
        ruido = np.random.normal(0, 2)
        score_atual = score_atual + tendencia + ruido
        score_atual = np.clip(score_atual, 0, 100)

        historico.append({
            "supplier_id": row["supplier_id"],
            "data_referencia": data.date(),
            "score_confiabilidade": round(score_atual, 2),
            "atraso_medio": round(row["atraso_medio"], 2),
            "perc_reclamacoes_abertas": round(row["perc_reclamacoes_abertas"], 2)
        })

# =========================
# DATAFRAME FINAL
# =========================
df = pd.DataFrame(historico)

# CLASSIFICAÇÃO DE RISCO
df["classificacao_risco"] = pd.cut(
    df["score_confiabilidade"],
    bins=[-1, 59, 79, 100],
    labels=["Alto Risco", "Atenção", "Confiável"]
)

# =========================
# SALVAR NA REFINED
# =========================
df.to_csv(
    "data/refined/supplier_reliability_score.csv",
    index=False
)

print("✔ Score histórico mensal (12 meses) gerado com sucesso")

