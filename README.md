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

## 🚀 How to Run
1. Clone the repo
2. Edit `config.py` with DB connection info
3. Run `main.py`
