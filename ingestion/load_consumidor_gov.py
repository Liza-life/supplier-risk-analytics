import pandas as pd
import numpy as np
from faker import Faker

fake = Faker("pt_BR")
np.random.seed(42)

def generate_consumidor_gov(n=1000):
    registros = []

    for _ in range(n):
        registros.append({
            "cnpj": fake.cnpj(),
            "empresa": fake.company(),
            "status_reclamacao": np.random.choice(
                ["Resolvida", "Não Resolvida"], p=[0.75, 0.25]
            ),
            "tempo_resposta_dias": np.random.randint(1, 30),
            "avaliacao_consumidor": np.random.randint(1, 6),
            "data_reclamacao": fake.date_between(start_date="-2y", end_date="today")
        })

    return pd.DataFrame(registros)

if __name__ == "__main__":
    df = generate_consumidor_gov()
    df.to_csv("data/raw/consumidor_gov.csv", index=False)
    print("✔ Dados de reclamações (Consumidor.gov) gerados na camada RAW")
