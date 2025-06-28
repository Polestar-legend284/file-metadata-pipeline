import sqlite3
db = 'metadata.db'
conn = sqlite3.connect(db)
rows = conn.cursor().execute(
    'SELECT name, size, ftype, uploaded_at FROM file_metadata'
).fetchall()
conn.close()
print(f"Rows in {db}:")
print(rows)