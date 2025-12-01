# api/database.py
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]  # project root
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "vuln_db.json"

DATA_DIR.mkdir(parents=True, exist_ok=True)

def load_db():
    if not DB_PATH.exists():
        DB_PATH.write_text("[]", encoding="utf-8")
        return []
    try:
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        # If file corrupted, reset to empty list
        DB_PATH.write_text("[]", encoding="utf-8")
        return []

def save_db(data):
    DB_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")

