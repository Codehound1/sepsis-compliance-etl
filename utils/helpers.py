def flag_compliance(df):
    df["CulturesBeforeAbxFlag"] = df["BloodCultureTime"] < df["AntibioticTime"]
    df["Antibiotic3hrFlag"] = (df["AntibioticTime"] - df["SepsisTimeZero"]).dt.total_seconds() <= 10800
    df["Lactate3hrFlag"] = (df["LactateTime"] - df["SepsisTimeZero"]).dt.total_seconds() <= 10800
    df["ComplianceMet"] = df["CulturesBeforeAbxFlag"] & df["Antibiotic3hrFlag"] & df["Lactate3hrFlag"]
    return df
