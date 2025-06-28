import os, sqlite3

print("Working dir:", os.getcwd())
print("DB file at:", os.path.abspath("metadata.db"))

conn = sqlite3.connect("metadata.db")
c = conn.cursor()

tables = c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
print("Tables:", tables)

try:
    rows = c.execute(
        "SELECT name,size,ftype,uploaded_at FROM file_metadata;"
    ).fetchall()
except sqlite3.OperationalError as e:
    rows = f"ERROR: {e}"
print("Rows in file_metadata:", rows)

conn.close()