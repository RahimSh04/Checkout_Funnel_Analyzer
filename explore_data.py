import pandas as pd

def load_clean_events():
    csv_file = "2019-Dec.csv"
    df = pd.read_csv(csv_file)
    df["event_time"] = pd.to_datetime(df["event_time"])
    df = df[["event_time", "event_type", "user_id"]]
    df["event_type"] = df["event_type"].replace({"cart": "add_to_cart"})
    df = df.rename(columns={"event_time": "timestamp"})
    df = df[df["event_type"].isin(["view", "add_to_cart", "purchase"])]
    df = df.drop_duplicates()
    return df
    

# print(df.columns)
# print(df["event_type"].unique())
# print(df.head())
# print(df.shape)
# print(df["user_id"].nunique())
# print(df.duplicated(subset=["user_id", "event_type"]).sum())
