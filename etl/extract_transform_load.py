import pandas as pd
from utils.helpers import flag_compliance

# Load data
df = pd.read_csv("data/sample_clarity_data.csv", parse_dates=["SepsisTimeZero", "LactateTime", "BloodCultureTime", "AntibioticTime"])

# Transform: Apply compliance rules
df = flag_compliance(df)

# Save output
df.to_excel("reports/compliance_summary.xlsx", index=False)
print("ETL Complete: compliance_summary.xlsx generated.")
