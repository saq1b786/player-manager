import sqlite3 

conn = sqlite3.connect('players.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Players(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               position INTEGER DEFAULT 0,
               goals INTEGER DEFAULT 0)

''')
conn.commit()
cursor.close()