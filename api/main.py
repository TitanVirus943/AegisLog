# api/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from api.models import Vulnerability
from api import crud

app = FastAPI(title="LV-MTS Local Vulnerability API", version="0.1")

# optional: allow CLI (same machine) CORS if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/vulnerabilities")
def get_vulns():
    return crud.get_all()

@app.get("/vulnerabilities/{vuln_id}")
def get_vuln(vuln_id: int):
    v = crud.get_one(vuln_id)
    if not v:
        raise HTTPException(status_code=404, detail="Vulnerability not found")
    return v

@app.post("/vulnerabilities", status_code=201)
def create_vuln(vuln: Vulnerability):
    created = crud.create(vuln)
    return created

@app.put("/vulnerabilities/{vuln_id}")
def update_vuln(vuln_id: int, vuln: Vulnerability):
    updated = crud.update(vuln_id, vuln)
    if not updated:
        raise HTTPException(status_code=404, detail="Vulnerability not found")
    return updated

@app.delete("/vulnerabilities/{vuln_id}")
def delete_vuln(vuln_id: int):
    ok = crud.delete(vuln_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Vulnerability not found")
    return {"deleted": vuln_id}


