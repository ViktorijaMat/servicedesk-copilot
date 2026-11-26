import pandas as pd
from datasets import load_dataset

ds = load_dataset("Tobi-Bueck/customer-support-tickets")

df = pd.DataFrame(ds["train"])

print(df["queue"].nunique())