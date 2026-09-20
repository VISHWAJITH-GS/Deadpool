import sqlite3
import os
from typing import Optional, Dict, Any
from app.config import config

class AppWebRegistry:
    def __init__(self, db_path: str = None):
        self.db_path = db_path or config.DB_PATH
        self._ensure_db_exists()
        self._init_db()

    def _ensure_db_exists(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            # App Registry
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS apps (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    executable TEXT NOT NULL
                )
            ''')
            # Website Registry
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS websites (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    url TEXT NOT NULL
                )
            ''')
            conn.commit()
            self._seed_initial_data()

    def _seed_initial_data(self):
        """Seed common default applications and websites."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            # Default Apps
            default_apps = [
                ("chrome", "Google Chrome", "chrome.exe"),
                ("edge", "Microsoft Edge", "msedge.exe"),
                ("notepad", "Notepad", "notepad.exe"),
                ("calc", "Calculator", "calc.exe"),
                ("explorer", "File Explorer", "explorer.exe"),
                ("vscode", "Visual Studio Code", "Code.exe"),
                ("word", "Microsoft Word", "winword.exe"),
                ("microsoftword", "Microsoft Word", "winword.exe"),
                ("paint", "Paint", "mspaint.exe")
            ]
            cursor.executemany("INSERT OR IGNORE INTO apps (id, name, executable) VALUES (?, ?, ?)", default_apps)
            
            # Default Websites
            default_websites = [
                ("leetcode", "LeetCode", "https://leetcode.com"),
                ("github", "GitHub", "https://github.com"),
                ("google", "Google", "https://google.com"),
                ("youtube", "YouTube", "https://youtube.com")
            ]
            cursor.executemany("INSERT OR IGNORE INTO websites (id, name, url) VALUES (?, ?, ?)", default_websites)
            conn.commit()

    def find_app(self, alias: str) -> Optional[str]:
        alias = alias.lower().replace(" ", "")
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT executable FROM apps WHERE id = ?", (alias,))
            result = cursor.fetchone()
            return result[0] if result else None

    def find_website(self, alias: str) -> Optional[str]:
        alias = alias.lower().replace(" ", "")
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT url FROM websites WHERE id = ?", (alias,))
            result = cursor.fetchone()
            return result[0] if result else None

app_web_registry = AppWebRegistry()
