import pandas as pd

METRICS_FILE = "data/metrics.csv"
metrics_df = pd.read_csv(METRICS_FILE, parse_dates=['date'])

def get_metrics(date_from=None, date_to=None, sort_by=None, order="asc", role="user"):
    df = metrics_df.copy()
    if date_from:
        df = df[df["date"] >= pd.to_datetime(date_from)]
    if date_to:
        df = df[df["date"] <= pd.to_datetime(date_to)]
    if sort_by and sort_by in df.columns:
        df = df.sort_values(by=sort_by, ascending=(order == "asc"))
    if role != "admin" and "cost_micros" in df.columns:
        df = df.drop(columns=["cost_micros"])
    return df
