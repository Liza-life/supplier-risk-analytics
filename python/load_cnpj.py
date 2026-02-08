import pandas as pd
import numpy as np
from faker import Faker

fake = Faker("pt_BR")
np.random.seed(42)

def generate_cnpj_data(n=300):
    portes = ["ME", "EPP", "Média", "Grande"]
    situacoes = ["Ativa", "Inativa"]

    registros = []

    for _ in range(n):
        registros.append({
            "cnpj": fake.cnpj(),
            "cnae": np.random.randint(1000, 9999),
            "porte_empresa": np.random.choice(portes, p=[0.4, 0.3, 0.2, 0.1]),
            "situacao_cadastral": np.random.choice(situacoes, p=[0.9, 0.1])
        })

    return pd.DataFrame(registros)

if __name__ == "__main__":
    df = generate_cnpj_data()
    df.to_csv("data/raw/cnpj.csv", index=False)
    print("✔ Dados CNPJ gerados na camada RAW")
