import sqlite3
from models import Player   

def create_tables() -> None:

    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS PLAYERS (
                   ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   NAME TEXT NOT NULL, 
                   POSITION TEXT NOT NULL, 
                   PHONE TEXT NULL, 
                   GOALS INT DEFAULT 0, 
                   TALLIES INT DEFAULT 0
                    )
    
    ''')
    conn.commit()
    conn.close()


def add_player(Player: Player) -> str:
    pass

