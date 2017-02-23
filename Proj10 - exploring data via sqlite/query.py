import sqlite3
conn = sqlite3.connect('factbook.db')
query = "select name from facts order by population asc;"
results = conn.execute(query).fetchmany(10)
print(results)
