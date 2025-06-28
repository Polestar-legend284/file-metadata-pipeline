import sqlite3
from datetime import datetime

DB = 'metadata.db'

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
      CREATE TABLE IF NOT EXISTS file_metadata (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        size INTEGER,
        ftype TEXT,
        uploaded_at TEXT
      );
    """)
    conn.commit()
    conn.close()

def insert_metadata(name, size, ftype):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    ts = datetime.now().isoformat()
    c.execute(
      'INSERT INTO file_metadata (name, size, ftype, uploaded_at) VALUES (?, ?, ?, ?)',
      (name, size, ftype, ts)
    )
    conn.commit()
    conn.close()