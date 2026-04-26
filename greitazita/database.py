import sqlite3
import os

class DatabaseManager:
    def __init__(self):
        self.db_path = "greitazita.db"
        self._init_db()
    
    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chat_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                salon_id INTEGER,
                user_message TEXT,
                ai_response TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        conn.close()
        print("✅ SQLite DB paruošta")
    
    def save_chat_message(self, salon_id: int, user_message: str, ai_response: str):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO chat_messages (salon_id, user_message, ai_response)
                VALUES (?, ?, ?)
            """, (salon_id, user_message, ai_response))
            conn.commit()
            conn.close()
            print(f"✅ Išsaugota į DB: salon_id={salon_id}")
        except Exception as e:
            print(f"❌ DB klaida: {e}")
    
    def get_all_messages(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM chat_messages")
        rows = cursor.fetchall()
        conn.close()
        return rows
