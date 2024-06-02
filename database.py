import sqlite3


con = sqlite3.connect("database.db")

if __name__ == '__main__':
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Comments (
    id INTEGER PRIMARY KEY,
    comment_id TEXT NOT NULL,
    body TEXT NOT NULL,
    author TEXT NOT NULL
    )""")
    con.commit()
    con.close()
