import os
import pandas as pd
from sqlalchemy import create_engine

# =========================
# CONEXÃO
# =========================
engine = create_engine(
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

# =========================
# CARREGAR DADOS
# =========================
cnpj = pd.read_csv("data/trusted/cnpj.csv")
score = pd.read_csv("data/refined/supplier_reliability_score.csv")

score["data_referencia"] = pd.to_datetime(score["data_referencia"])

# =========================
# DIM FORNECEDOR
# =========================
fornecedores_score = score[["supplier_id"]].drop_duplicates()

fornecedores_cnpj = (
    cnpj[["cnpj", "porte_empresa", "cnae"]]
    .rename(columns={"cnpj": "supplier_id"})
)

dim_fornecedor = fornecedores_score.merge(
    fornecedores_cnpj,
    on="supplier_id",
    how="left"
)

dim_fornecedor["porte_empresa"] = dim_fornecedor["porte_empresa"].fillna("Desconhecido")
dim_fornecedor["cnae"] = dim_fornecedor["cnae"].fillna(0).astype(int)

# =========================
# DIM TEMPO
# =========================
dim_tempo = score[["data_referencia"]].drop_duplicates()
dim_tempo["ano"] = dim_tempo["data_referencia"].dt.year
dim_tempo["mes"] = dim_tempo["data_referencia"].dt.month
dim_tempo["dia"] = dim_tempo["data_referencia"].dt.day
dim_tempo = dim_tempo.rename(columns={"data_referencia": "data_id"})

# =========================
# FATO
# =========================
fato = score[
    [
        "supplier_id",
        "data_referencia",
        "score_confiabilidade",
        "atraso_medio",
        "perc_reclamacoes_abertas",
        "classificacao_risco"
    ]
].rename(columns={"data_referencia": "data_id"})

# =========================
# CARGA (ORDEM CORRETA)
# =========================
dim_fornecedor.to_sql(
    "dim_fornecedor",
    engine,
    if_exists="append",
    index=False
)

dim_tempo.to_sql(
    "dim_tempo",
    engine,
    if_exists="append",
    index=False
)

fato.to_sql(
    "fato_confiabilidade_fornecedor",
    engine,
    if_exists="append",
    index=False
)

print("✔ Data Warehouse recarregado com sucesso (full refresh)")

