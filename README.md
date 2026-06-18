# Player Manager CLI

A command-line football squad management tool built with Python and SQLite. Track players, log tallies for late arrivals, and flag repeat offenders — inspired by a real problem managing weekly football sessions.

## Features

- Add players with name, position, and phone number
- View all registered players
- Add tallies to players who arrive late
- Automatically flag players with 3 or more tallies
- Delete players from the squad
- Persistent SQLite database — data survives between sessions

## How to Run

Make sure you have Python 3 installed, then:

```bash
python3 main.py
```

## Project Structure

player-manager/

main.py        — Entry point and menu interface

models.py      — Player dataclass

database.py    — SQLite database operations (CRUD)

players.db     — Auto-generated database file

## Built With

- Python 3
- SQLite3 (standard library)
- Dataclasses for structured data

## What I Learned

Third project in my learning journey, stepping up from JSON file storage to a proper database. Key things I learned:

- SQL operations: CREATE, INSERT, SELECT, UPDATE, DELETE
- Parameterised queries to prevent SQL injection
- Converting between database rows and Python objects
- Separating concerns across multiple files (models, database, interface)
- This project is a simplified prototype of a larger football session management app I'm building