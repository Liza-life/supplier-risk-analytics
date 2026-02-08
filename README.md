# Supplier Risk Analytics

End-to-end data analytics project focused on monitoring and analyzing supplier risk, combining data engineering, analytics modeling and executive-level dashboards.

---

## 📌 Project Overview

This project simulates a real-world **supplier risk intelligence system**, designed to support decision-making in procurement, compliance and operations.

The solution consolidates operational data (delays, complaints and performance scores), transforms it into analytical models and delivers actionable insights through interactive Power BI dashboards.

---

## 🏗️ Architecture

The project follows a modern analytics architecture:

Raw Data → Python ETL → PostgreSQL Data Warehouse → SQL Analytical Views → Power BI Dashboards

---

## 🗄️ Data Model

### Fact Table
- **fato_confiabilidade_fornecedor**
  - Supplier reliability score
  - Average delivery delay
  - Open complaints percentage
  - Risk classification
  - Date reference

### Dimension Tables
- **dim_fornecedor**
- **dim_tempo**

---

## 📊 Analytical Views

The analytics layer is built using SQL views to centralize business logic:

- **vw_executive_snapshot**
- **vw_supplier_risk_overview**
- **vw_supplier_risk_summary**
- **vw_supplier_risk_trend**
- **vw_supplier_risk_distribution**

These views ensure consistency and reusability across dashboards and analyses.

---

## 📈 Dashboards

### 1️⃣ Executive Risk Overview
- Total suppliers
- Average reliability score
- High-risk suppliers
- Monthly variation of high-risk suppliers
- Risk distribution (latest month)
- High-risk suppliers trend

### 2️⃣ Risk Analysis
- Score distribution by risk range
- Evolution of average score over time
- Risk concentration analysis

### 3️⃣ Critical Suppliers
- High-risk suppliers overview
- Average delay and score
- Top suppliers with highest operational impact

### 4️⃣ Operational Diagnostics
- Delay vs. score correlation
- Average delay by risk level
- Operational performance indicators

### 5️⃣ Trends and Projections
- Average score variation (last 6 months)
- Growth rate of high-risk suppliers
- Score deterioration velocity

---

## 🛠️ Technologies Used

- **Python** (Pandas, SQLAlchemy)
- **PostgreSQL**
- **Power BI**
- **SQL**
- **Git & GitHub**

---

## 🎯 Key Learnings

- Data modeling using star schema
- Building analytical SQL views
- Handling time-series data
- Designing executive and analytical dashboards
- Translating raw data into business insights

---

## 🚀 Future Improvements

- Incremental data ingestion
- Automated data pipelines
- Alert system for critical suppliers
- Predictive risk modeling
- Workflow orchestration with Airflow

---

## 👤 Author

**Lizandra Ruiz**  
Data Analytics & Data Engineering
