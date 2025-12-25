import os

ASSET_DB = "data/assets.txt"
VULN_DB = "data/vulns.txt"

os.makedirs("data", exist_ok=True)

# Initialize DB files if not exist
for db in [ASSET_DB, VULN_DB]:
    if not os.path.exists(db):
        with open(db, "w") as f:
            f.write("")

# ---- Asset DB Operations ----
def read_assets():
    assets = []
    with open(ASSET_DB, "r") as f:
        for line in f.readlines():
            if line.strip():
                parts = line.strip().split("|")
                assets.append({
                    "id": int(parts[0]),
                    "name": parts[1],
                    "ip": parts[2],
                    "os": parts[3]
                })
    return assets

def get_next_asset_id():
    assets = read_assets()
    if not assets:
        return 1
    return max(a["id"] for a in assets) + 1


def write_asset(asset):
    # assign id if not provided
    if "id" not in asset or asset.get("id") is None:
        asset["id"] = get_next_asset_id()
    with open(ASSET_DB, "a") as f:
        f.write(f"{asset['id']}|{asset['name']}|{asset['ip']}|{asset['os']}\n")
    return asset["id"]

def delete_asset_db(aid):
    assets = read_assets()
    assets = [a for a in assets if a["id"] != aid]
    with open(ASSET_DB, "w") as f:
        for a in assets:
            f.write(f"{a['id']}|{a['name']}|{a['ip']}|{a['os']}\n")


def update_asset_db(aid, payload):
    assets = read_assets()
    for a in assets:
        if a["id"] == aid:
            a.update(payload)
    with open(ASSET_DB, "w") as f:
        for a in assets:
            f.write(f"{a['id']}|{a['name']}|{a['ip']}|{a['os']}\n")

# ---- Vulnerability DB Operations ----
def read_vulns():
    vulns = []
    with open(VULN_DB, "r") as f:
        for line in f.readlines():
            if line.strip():
                parts = line.strip().split("|")
                vulns.append({
                    "id": int(parts[0]),
                    "title": parts[1],
                    "severity": parts[2],
                    "asset_id": int(parts[3]),
                    "description": parts[4],
                    "status": parts[5]
                })
    return vulns

def write_vuln(vuln):
    # ensure id assignment handled by caller or assign here
    if "id" not in vuln or vuln.get("id") is None:
        vulns = read_vulns()
        vuln["id"] = 1 if not vulns else max(v["id"] for v in vulns) + 1
    with open(VULN_DB, "a") as f:
        f.write(f"{vuln['id']}|{vuln['title']}|{vuln['severity']}|{vuln['asset_id']}|{vuln['description']}|{vuln['status']}\n")

def update_vuln_db(vid, payload):
    vulns = read_vulns()
    for v in vulns:
        if v["id"] == vid:
            v.update(payload)
    with open(VULN_DB, "w") as f:
        for v in vulns:
            f.write(f"{v['id']}|{v['title']}|{v['severity']}|{v['asset_id']}|{v['description']}|{v['status']}\n")

def delete_vuln_db(vid):
    vulns = read_vulns()
    vulns = [v for v in vulns if v["id"] != vid]
    with open(VULN_DB, "w") as f:
        for v in vulns:
            f.write(f"{v['id']}|{v['title']}|{v['severity']}|{v['asset_id']}|{v['description']}|{v['status']}\n")
