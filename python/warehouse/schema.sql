-- =========================
-- DIMENSÃO FORNECEDOR
-- =========================
CREATE TABLE IF NOT EXISTS dim_fornecedor (
    supplier_id VARCHAR(14) PRIMARY KEY,
    porte_empresa VARCHAR(20),
    cnae INT
);

-- =========================
-- DIMENSÃO TEMPO
-- =========================
CREATE TABLE IF NOT EXISTS dim_tempo (
    data_id DATE PRIMARY KEY,
    ano INT,
    mes INT,
    dia INT
);

-- =========================
-- FATO CONFIABILIDADE
-- =========================
CREATE TABLE IF NOT EXISTS fato_confiabilidade_fornecedor (
    supplier_id VARCHAR(14),
    data_id DATE,
    score_confiabilidade NUMERIC(5,2),
    atraso_medio NUMERIC(5,2),
    perc_reclamacoes_abertas NUMERIC(5,2),
    classificacao_risco VARCHAR(20),

    CONSTRAINT fk_fornecedor
        FOREIGN KEY (supplier_id)
        REFERENCES dim_fornecedor (supplier_id),

    CONSTRAINT fk_tempo
        FOREIGN KEY (data_id)
        REFERENCES dim_tempo (data_id)
);
