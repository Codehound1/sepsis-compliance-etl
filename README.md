# Sepsis Compliance ETL Project

This project extracts, transforms, and loads Epic Clarity/Caboodle data to generate compliance metrics for Severe Sepsis and Septic Shock quality reporting. Includes a sample Power BI dashboard.

## 📊 Objective
Track whether patients received:
- Initial lactate within 3 hours
- Antibiotics within 3 hours
- Blood cultures before antibiotics

## 🔁 ETL Flow

1. **Extract:** Pull patient encounter + lab result data (e.g., Hgb, Lactate, Cultures)
2. **Transform:** Flag compliance based on CMS guidelines
3. **Load:** Output Excel & CSV summaries for dashboarding

## 🚀 Usage

```bash
# 1. Set up virtual env (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the ETL
python etl/extract_transform_load.py
```

## 📈 Dashboard

Open `dashboard/sepsis_dashboard.pbit` in Power BI Desktop.

## 📂 Folder Guide

| Folder     | Contents                            |
|------------|-------------------------------------|
| `etl/`     | Core ETL script                     |
| `data/`    | Raw or mock Clarity CSVs            |
| `reports/` | Output: compliance % summaries      |
| `dashboard/`| Power BI dashboard template        |
| `utils/`   | Helper functions (e.g., date parsing)|

## 📌 Note

This repo is for educational/demo use. Replace the mock data with your own Clarity/Caboodle extracts.
