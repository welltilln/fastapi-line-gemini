import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "sessions.db")

def init_db():
    """Initialize the SQLite database and create the sessions table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            user_id TEXT PRIMARY KEY,
            history TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_session_history(user_id: str) -> list:
    """Retrieve the chat history for a given user. Returns a list (can be empty)."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT history FROM sessions WHERE user_id = ?', (user_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row is None or not row[0]:
        return []
    
    try:
        return json.loads(row[0])
    except json.JSONDecodeError:
        return []

def save_session_history(user_id: str, history: list):
    """Save the chat history list as a JSON string to the database."""
    history_json = json.dumps(history)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO sessions (user_id, history)
        VALUES (?, ?)
        ON CONFLICT(user_id) DO UPDATE SET history = excluded.history
    ''', (user_id, history_json))
    conn.commit()
    conn.close()

# Initialize the db when module is imported
init_db()
