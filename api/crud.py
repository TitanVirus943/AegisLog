# api/crud.py
from api.database import load_db, save_db
from api.models import Vulnerability

def next_id(db):
    if not db:
        return 1
    return max(item.get("id", 0) for item in db) + 1

def get_all():
    return load_db()

def get_one(vuln_id):
    db = load_db()
    for v in db:
        if v.get("id") == vuln_id:
            return v
    return None

def create(vuln):
    db = load_db()
    vuln_dict = vuln.dict()
    vuln_dict["id"] = next_id(db)
    db.append(vuln_dict)
    save_db(db)
    return vuln_dict

def update(vuln_id, vuln):
    db = load_db()
    for i, v in enumerate(db):
        if v.get("id") == vuln_id:
            new = vuln.dict()
            new["id"] = vuln_id
            db[i] = new
            save_db(db)
            return new
    return None

def delete(vuln_id):
    db = load_db()
    new_db = [v for v in db if v.get("id") != vuln_id]
    if len(new_db) == len(db):
        return False
    save_db(new_db)
    return True

