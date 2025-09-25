import pandas as pd

USERS_FILE = "data/users.csv"
users_df = pd.read_csv(USERS_FILE)

def authenticate(email, password):
    user = users_df[(users_df["email"] == email) & (users_df["password"] == password)]
    if user.empty:
        return None
    return user.iloc[0].to_dict()
