import pandas as pd
import sqlite3

con = sqlite3.connect("./data/incidents.db")

print(pd.read_sql_query("SELECT COUNT(*) FROM inc", con)) #count how many tickets there are in total

print(pd.read_sql_query("SELECT priority, COUNT(*) FROM inc GROUP BY Priority", con)) #count tickets based on priority

result = pd.read_sql_query("SELECT queue, COUNT(*) as evr FROM inc WHERE language = 'en' GROUP BY queue ORDER BY evr DESC LIMIT 5", con) #prints top 5 english queues

con.close()