from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
DB = 'metadata.db'

def fetch_all():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('SELECT name,size,ftype,uploaded_at FROM file_metadata ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    return rows

@app.route('/')
def index():
    return render_template('index.html', files=fetch_all())

if __name__ == '__main__':
    app.run(debug=True)