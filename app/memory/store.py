import sqlite3
import os
from typing import List, Dict, Any
from app.config import config

class MemoryStore:
    def __init__(self, db_path: str = None):
        self.db_path = db_path or config.DB_PATH
        self._ensure_db_exists()
        self._init_db()

    def _ensure_db_exists(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS explicit_memories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()

    def add_memory(self, content: str) -> int:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO explicit_memories (content) VALUES (?)", (content,))
            conn.commit()
            return cursor.lastrowid

    def get_all_memories(self) -> List[Dict[str, Any]]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT id, content, timestamp FROM explicit_memories ORDER BY timestamp DESC")
            return [dict(row) for row in cursor.fetchall()]

    def delete_memory(self, memory_id: int) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM explicit_memories WHERE id = ?", (memory_id,))
            conn.commit()
            return cursor.rowcount > 0

memory_store = MemoryStore()
