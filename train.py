import pandas as pd
import sqlite3

con = sqlite3.connect("./data/incidents.db")

df = pd.read_sql_query("SELECT subject, body, queue FROM inc WHERE language = 'en'", con)

print(df) #all values

print("Missing values = ", df.isnull().sum()) #missing value sum

df["subject"] = df["subject"].fillna("")

df["body"] = df["body"].fillna("")

df["text"] = df["subject"] + " " + df["body"]

print("Missing text values = ", df["text"].isnull().sum())

con.close()