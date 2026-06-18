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


def add_player(player: Player) -> str:

    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO PLAYERS (NAME, POSITION, PHONE)
    VALUES (?, ?, ?)

''', (player.name, player.position, player.phone))

    conn.commit()
    conn.close()
    return 'Player added to the database!'


def get_all_players() -> list:
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()
    player_list = []

    cursor.execute('SELECT * FROM PLAYERS')
    all_players = cursor.fetchall()

    for player in all_players:
        player_list.append(Player(player[1], player[2], player[3], player[4], player[5], player[0]))

    conn.close()

    return player_list


def add_tally(name: str):
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE PLAYERS SET TALLIES = TALLIES +1 WHERE NAME = ?


''', (name,))
    conn.commit()
    conn.close()

