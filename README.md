
![GitHub last commit](https://img.shields.io/github/last-commit/Codehound1/sepsis-compliance-etl)
![GitHub repo size](https://img.shields.io/github/repo-size/Codehound1/sepsis-compliance-etl)
![Power BI Template](https://img.shields.io/badge/PowerBI-SepsisTemplate-blue)

# sepsis-compliance-etl
# Sepsis Compliance Data Pipeline

## 🩺 Problem
Hospitals must report on timely care for patients with sepsis and septic shock. This project extracts clinical data, calculates compliance with SEP-1 measures, and visualizes results.

## 🧠 Solution
- Extracted encounter and patient data from Epic Caboodle
- Applied SEP-1 measure logic for lactate, blood cultures, and antibiotics
- Calculated compliance flags and exported to dashboard-ready format

## 🛠 Tech Stack
- SQL (Caboodle)
- Python (Pandas)
- PostgreSQL
- Excel / Power BI
- GitHub for version control

## 📈 Sample Output
![Dashboard](architecture_diagram.png)
## 📈 Dashboard

This project includes a Power BI dashboard template for visualizing sepsis bundle compliance performance.

### 📊 Visuals Included
- **Clustered Column Chart** – % ComplianceMet by Month
- **Table** – MRN and Compliance Flags (Cultures, Antibiotics, Lactate)
- **Donut Chart** – Overall Compliance vs Non-Compliance

### 📂 File
[`SepsisComplianceTemplate.pbit`](dashboard/SepsisComplianceTemplate.pbit)

### 🧪 How to Use
1. Open the `.pbit` file in Power BI Desktop
2. When prompted, connect it to your most recent `compliance_summary.xlsx` file
3. Explore and customize visuals as needed

> Template created as part of a data engineering portfolio project integrating Epic Clarity data.

## 🚀 How to Run
1. Clone the repo
2. Edit `config.py` with DB connection info
3. Run `main.py`
