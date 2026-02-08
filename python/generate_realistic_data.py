import pandas as pd
import numpy as np
from datetime import datetime

np.random.seed(42)

N_FORNECEDORES = 2000
MESES = pd.date_range(end=datetime.today(), periods=12, freq="MS")

# ------------------------
# FORNECEDORES
# ------------------------
suppliers = pd.DataFrame({
    "supplier_id": np.arange(100000000001, 100000000001 + N_FORNECEDORES)
})

suppliers["perfil"] = np.random.choice(
    ["Confiável", "Atenção", "Alto Risco"],
    size=N_FORNECEDORES,
    p=[0.7, 0.2, 0.1]
)

# ------------------------
# HISTÓRICO MENSAL
# ------------------------
records = []

for _, row in suppliers.iterrows():
    perfil = row["perfil"]
    score_base = {
        "Confiável": np.random.uniform(88, 95),
        "Atenção": np.random.uniform(72, 82),
        "Alto Risco": np.random.uniform(55, 68),
    }[perfil]

    for mes in MESES:
        atraso = {
            "Confiável": np.random.uniform(0, 2),
            "Atenção": np.random.uniform(3, 6),
            "Alto Risco": np.random.uniform(7, 15),
        }[perfil]

        reclamacoes = {
            "Confiável": np.random.uniform(0, 1),
            "Atenção": np.random.uniform(1, 5),
            "Alto Risco": np.random.uniform(5, 20),
        }[perfil]

        ruido = np.random.normal(0, 2)

        score = max(
            40,
            min(
                98,
                score_base
                - atraso * 2.5
                - reclamacoes * 1.8
                + ruido,
            ),
        )

        classificacao = (
            "Confiável" if score >= 85
            else "Atenção" if score >= 70
            else "Alto Risco"
        )

        records.append({
            "supplier_id": row["supplier_id"],
            "data_id": mes.strftime("%Y-%m-%d"),
            "atraso_medio": round(atraso, 1),
            "perc_reclamacoes_abertas": round(reclamacoes, 2),
            "score_confiabilidade": round(score, 2),
            "classificacao_risco": classificacao,
        })

fato = pd.DataFrame(records)

# ------------------------
# EXPORTAÇÃO
# ------------------------
fato.to_csv("data/raw/fato_confiabilidade_fornecedor.csv", index=False)

print("Dados realistas gerados com sucesso.")
