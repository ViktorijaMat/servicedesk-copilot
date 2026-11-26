import pandas as pd
from datasets import load_dataset
import sqlite3

ds = load_dataset("Tobi-Bueck/customer-support-tickets")

con = sqlite3.connect("./data/incidents.db")

df = pd.DataFrame(ds["train"])

df.to_sql("inc", con, if_exists="replace")

con.close()