-- ===============================
-- VIEW EXECUTIVA (1 LINHA)
-- ===============================
CREATE OR REPLACE VIEW vw_executive_snapshot AS
WITH ultimo_mes AS (
    SELECT MAX(data_id) AS data_ref
    FROM fato_confiabilidade_fornecedor
)
SELECT
    COUNT(DISTINCT supplier_id) AS total_fornecedores,
    ROUND(AVG(score_confiabilidade), 2) AS score_medio_atual,
    COUNT(DISTINCT CASE WHEN classificacao_risco = 'Alto Risco' THEN supplier_id END)
        AS fornecedores_alto_risco
FROM fato_confiabilidade_fornecedor f
JOIN ultimo_mes u ON f.data_id = u.data_ref;


-- ===============================
-- DISTRIBUIÇÃO POR RISCO (EXECUTIVO)
-- ===============================
CREATE OR REPLACE VIEW vw_supplier_risk_overview AS
WITH ultimo_mes AS (
    SELECT MAX(data_id) AS data_ref
    FROM fato_confiabilidade_fornecedor
)
SELECT
    classificacao_risco,
    COUNT(DISTINCT supplier_id) AS total_fornecedores
FROM fato_confiabilidade_fornecedor f
JOIN ultimo_mes u ON f.data_id = u.data_ref
GROUP BY classificacao_risco;


-- ===============================
-- TENDÊNCIA TEMPORAL
-- ===============================
CREATE OR REPLACE VIEW vw_supplier_risk_trend AS
SELECT
    data_id,
    ROUND(AVG(score_confiabilidade), 2) AS score_medio_dia,
    COUNT(DISTINCT CASE WHEN classificacao_risco = 'Alto Risco' THEN supplier_id END)
        AS qtd_fornecedores_alto_risco
FROM fato_confiabilidade_fornecedor
GROUP BY data_id
ORDER BY data_id;

-- ============================================
-- DISTRIBUIÇÃO DE FORNECEDORES POR RISCO
-- (ÚLTIMO MÊS) — FORMATO CATEGÓRICO
-- ============================================
CREATE OR REPLACE VIEW vw_supplier_risk_distribution AS
WITH ultimo_mes AS (
    SELECT MAX(data_id) AS data_ref
    FROM fato_confiabilidade_fornecedor
)
SELECT
    classificacao_risco,
    COUNT(DISTINCT supplier_id) AS total_fornecedores
FROM fato_confiabilidade_fornecedor f
JOIN ultimo_mes u
  ON f.data_id = u.data_ref
GROUP BY classificacao_risco;

