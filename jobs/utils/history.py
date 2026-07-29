import sqlite3
from pathlib import Path

DATA_DIR = Path(__file__).parent / "../data"
DATA_DIR.mkdir(exist_ok=True)
DB_NAME = DATA_DIR / "jobs.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_tables():
    # o jobs-cli --help não cria o banco, precisa ser algo do tipo jobs-cli search
    # print(f"Criando banco em: {DB_NAME}")
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                command TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

def save_history(command: str):
    with get_connection() as conn:
        conn.execute(
            """
            INSERT INTO history(command)
            VALUES (?)
            """,
            (command,),
        )

def all_commands():
    with get_connection() as conn:
        cursor = conn.execute("SELECT command, created_at FROM history ORDER BY created_at DESC")
        return cursor.fetchall()