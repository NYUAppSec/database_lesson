import pandas as pd
import sqlite3
import sys

# Parse the table name from the first argument
table_name = sys.argv[1]

df = pd.read_csv(table_name + '.csv')

# Connect to the SQLite database
conn = sqlite3.connect(table_name + '.db')

# Write the DataFrame to SQLite
df.to_sql(table_name, conn, if_exists='replace', index=False)

# Close the connection
conn.close()
