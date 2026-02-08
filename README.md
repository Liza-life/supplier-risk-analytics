Análise de Risco de Fornecedores

Supplier Risk Analytics – Data Engineering & Analytics Project

Projeto completo de engenharia e análise de dados ponta a ponta, focado no monitoramento, diagnóstico e projeção de risco de fornecedores, combinando ETL em Python, Data Warehouse em PostgreSQL, modelagem analítica e dashboards executivos no Power BI.

🎯 Objetivo do Projeto

Construir um sistema analítico capaz de:

Avaliar a confiabilidade de fornecedores

Identificar fornecedores críticos e em alto risco

Monitorar tendências de deterioração do score

Apoiar decisão executiva e gestão operacional

O projeto simula um cenário real corporativo, com dados realistas, regras de negócio claras e arquitetura escalável.

🧱 Arquitetura da Solução
Dados CSV (Raw / Trusted)
        ↓
ETL em Python (limpeza, enriquecimento e scoring)
        ↓
PostgreSQL (Data Warehouse – modelo dimensional)
        ↓
Views Analíticas
        ↓
Power BI (Dashboards Executivos e Operacionais)

🗂️ Estrutura do Repositório
supplier-risk-analytics/
│
│ python/
│   ├data_cleaning.py
│   ├generate_realistic_data.py
│   ├reliability_score.py
│   ├load_dw.py
│
├sql/
│   ├schema.sql
│   ├tables.sql
│   └views.sql
│
├data/
│   └sample/
│       └README.md
│
├docs/
│   ├dashboard_visao_executiva.png
│   ├dashboard_diagnostico_operacional.png
│   ├dashboard_fornecedores_criticos.png
│   └dashboard_tendencias.png
│
├.env.example
├.gitignore
├requirements.txt
└README.md

🧪 Dados Utilizados

CNPJ / fornecedores (simulado com base em estrutura real)

Atraso médio

Percentual de reclamações abertas

Score de confiabilidade

Classificação de risco:

Confiável

Atenção

Alto Risco

⚠️ Os dados reais não são versionados por questões de privacidade.
O projeto inclui geração de dados realistas para simulação.

🧮 Modelagem de Dados
🔹 Dimensões

dim_fornecedor

dim_tempo

🔹 Fato

fato_confiabilidade_fornecedor

Modelo dimensional desenhado para análises históricas, comparativas e de tendência.

🔄 Estratégia de Carga (ETL)
✔ Dimensões

Carga idempotente

Evita duplicidade de chaves

Pode ser executada múltiplas vezes sem erro

✔ Fato

Full refresh controlado

Garante consistência analítica

Essa abordagem reflete boas práticas reais de Data Warehousing.

📊 Dashboards (Power BI)
🔹 1. Visão Executiva – Risco de Fornecedores

Total de fornecedores

Score médio atual

Quantidade em alto risco

Variação mensal de risco

Distribuição por classificação

Evolução temporal de fornecedores críticos

🔹 2. Análise de Risco de Fornecedores

Distribuição por faixa de score

Relação entre score e atraso

Tendência de queda do score médio

🔹 3. Fornecedores Críticos

Top fornecedores em alto risco

Ranking por atraso médio

Score médio dos críticos

Lista priorizada para ação

🔹 4. Diagnóstico Operacional do Risco

Atraso médio por nível de risco

Impacto operacional no score

Relação atraso × confiabilidade

🔹 5. Tendências e Projeções

Variação do score médio (últimos meses)

Crescimento de fornecedores em alto risco

Velocidade de deterioração do score

🧠 Principais Insights Gerados

Crescimento acelerado de fornecedores em alto risco

Queda consistente do score médio ao longo do tempo

Forte correlação entre atraso médio e deterioração do score

Fornecedores críticos concentrados em faixas intermediárias antes de colapsar

⚙️ Tecnologias Utilizadas

Python (pandas, SQLAlchemy)

PostgreSQL

SQL (modelagem e views analíticas)

Power BI

Git & GitHub

🚀 Como Executar o Projeto

1️⃣ Clone o repositório:

git clone https://github.com/Liza-life/supplier-risk-analytics.git


2️⃣ Configure as variáveis de ambiente:

cp .env.example .env


3️⃣ Instale as dependências:

pip install -r requirements.txt


4️⃣ Execute o pipeline:

python python/load_dw.py


5️⃣ Conecte o Power BI ao PostgreSQL e explore os dashboards.

💼 Contexto Profissional

Este projeto foi desenvolvido com foco em:

Portfólio profissional

Cenários reais de negócio

Boas práticas de engenharia de dados

Comunicação analítica para tomada de decisão

👩‍💻 Autora

Lizandra Ruiz
Engenharia de Dados | Analytics | BI
