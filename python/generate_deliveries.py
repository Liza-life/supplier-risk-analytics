import pandas as pd
import numpy as np
from faker import Faker

fake = Faker("pt_BR")
np.random.seed(42)

def generate_deliveries(n=2000):
    registros = []

    for _ in range(n):
        atraso = np.random.choice(
            [0, 1, 2, 3, 5, 10],
            p=[0.4, 0.2, 0.15, 0.1, 0.1, 0.05]
        )

        data_prevista = fake.date_between(start_date="-1y", end_date="-1m")
        data_real = pd.to_datetime(data_prevista) + pd.to_timedelta(atraso, unit="D")

        registros.append({
            "supplier_id": fake.cnpj(),
            "order_id": fake.uuid4(),
            "data_prevista": data_prevista,
            "data_real": data_real.date(),
            "atraso_dias": atraso,
            "pedido_completo": np.random.choice([True, False], p=[0.9, 0.1])
        })

    return pd.DataFrame(registros)

if __name__ == "__main__":
    df = generate_deliveries()
    df.to_csv("data/raw/entregas.csv", index=False)
    print("✔ Histórico de entregas gerado na camada RAW")
