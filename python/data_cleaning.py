import pandas as pd

def clean_cnpj(cnpj):
    if pd.isna(cnpj):
        return None
    return "".join(filter(str.isdigit, str(cnpj)))

if __name__ == "__main__":
    consumidor = pd.read_csv("data/raw/consumidor_gov.csv")
    cnpj = pd.read_csv("data/raw/cnpj.csv")
    entregas = pd.read_csv("data/raw/entregas.csv")

    # Padronização de CNPJ
    consumidor["cnpj"] = consumidor["cnpj"].apply(clean_cnpj)
    cnpj["cnpj"] = cnpj["cnpj"].apply(clean_cnpj)
    entregas["supplier_id"] = entregas["supplier_id"].apply(clean_cnpj)

    # Tipos de dados
    consumidor["data_reclamacao"] = pd.to_datetime(consumidor["data_reclamacao"])
    entregas["data_prevista"] = pd.to_datetime(entregas["data_prevista"])
    entregas["data_real"] = pd.to_datetime(entregas["data_real"])

    # Remover duplicados
    consumidor.drop_duplicates(inplace=True)
    cnpj.drop_duplicates(inplace=True)
    entregas.drop_duplicates(inplace=True)

    # Salvar na camada TRUSTED
    consumidor.to_csv("data/trusted/consumidor_gov.csv", index=False)
    cnpj.to_csv("data/trusted/cnpj.csv", index=False)
    entregas.to_csv("data/trusted/entregas.csv", index=False)

    print("✔ Dados limpos e padronizados salvos na camada TRUSTED")
