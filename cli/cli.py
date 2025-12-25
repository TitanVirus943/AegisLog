import requests
from tabulate import tabulate
import sys

API_BASE = "http://127.0.0.1:8080"


def list_assets():
    r = requests.get(f"{API_BASE}/assets")
    assets = r.json()
    if not assets:
        print("No assets found")
        return
    print(tabulate([[a["id"], a["name"], a["ip"], a["os"]] for a in assets],
                   headers=["ID", "Name", "IP", "OS"], tablefmt="fancy_grid"))


def add_asset():
    print("\n--- Add Asset ---")
    asset = {
        "name": input("Name: "),
        "ip": input("IP: "),
        "os": input("OS: ")
    }
    r = requests.post(f"{API_BASE}/assets", json=asset)
    try:
        print(r.json())
    except Exception:
        print(r.text)


def update_asset():
    print("\n--- Update Asset ---")
    aid = int(input("Asset ID: "))
    r = requests.get(f"{API_BASE}/assets")
    assets = r.json()
    asset = next((a for a in assets if a["id"] == aid), None)
    if not asset:
        print("Asset not found")
        return
    name = input(f"Name [{asset['name']}]: ") or asset['name']
    ip = input(f"IP [{asset['ip']}]: ") or asset['ip']
    os_ = input(f"OS [{asset['os']}]: ") or asset['os']
    payload = {"name": name, "ip": ip, "os": os_}
    r = requests.put(f"{API_BASE}/assets/{aid}", json=payload)
    try:
        print(r.json())
    except Exception:
        print(r.text)


def delete_asset():
    aid = int(input("Asset ID to delete: "))
    r = requests.delete(f"{API_BASE}/assets/{aid}")
    try:
        print(r.json())
    except Exception:
        print(r.text)


def list_vulns():
    r = requests.get(f"{API_BASE}/vulnerabilities")
    vulns = r.json()
    if not vulns:
        print("No vulnerabilities found")
        return
    print(tabulate([[v.get("id"), v.get("title"), v.get("severity"), v.get("asset_id"), v.get("status")] for v in vulns],
                   headers=["ID", "Title", "Severity", "AssetID", "Status"], tablefmt="fancy_grid"))


def add_vuln():
    print("\n--- Add Vulnerability ---")
    vuln = {
        "title": input("Title: "),
        "severity": input("Severity: "),
        "asset_id": int(input("Asset ID: ")),
        "description": input("Description: "),
        "status": input("Status (open/closed): ") or "open"
    }
    r = requests.post(f"{API_BASE}/vulnerabilities", json=vuln)
    try:
        print(r.json())
    except Exception:
        print(r.text)


def update_vuln():
    print("\n--- Update Vulnerability ---")
    vid = int(input("Vuln ID: "))
    r = requests.get(f"{API_BASE}/vulnerabilities")
    vulns = r.json()
    v = next((x for x in vulns if x.get("id") == vid), None)
    if not v:
        print("Vulnerability not found")
        return
    title = input(f"Title [{v.get('title')}]: ") or v.get('title')
    severity = input(f"Severity [{v.get('severity')}]: ") or v.get('severity')
    asset_id = input(f"Asset ID [{v.get('asset_id')}]: ") or v.get('asset_id')
    description = input(f"Description [{v.get('description')}]: ") or v.get('description')
    status = input(f"Status [{v.get('status')}]: ") or v.get('status')
    payload = {
        "title": title,
        "severity": severity,
        "asset_id": int(asset_id),
        "description": description,
        "status": status
    }
    r = requests.put(f"{API_BASE}/vulnerabilities/{vid}", json=payload)
    try:
        print(r.json())
    except Exception:
        print(r.text)


def delete_vuln():
    vid = int(input("Vuln ID to delete: "))
    r = requests.delete(f"{API_BASE}/vulnerabilities/{vid}")
    try:
        print(r.json())
    except Exception:
        print(r.text)


def main_menu():
    while True:
        print("\n===== LV-MTS Security Tracker CLI =====")
        print("1. List Assets")
        print("2. Add Asset")
        print("3. Update Asset")
        print("4. Delete Asset")
        print("5. List Vulnerabilities")
        print("6. Add Vulnerability")
        print("7. Update Vulnerability")
        print("8. Delete Vulnerability")
        print("0. Exit")

        c = input("Select: ")

        if c == "1":
            list_assets()
        elif c == "2":
            add_asset()
        elif c == "3":
            update_asset()
        elif c == "4":
            delete_asset()
        elif c == "5":
            list_vulns()
        elif c == "6":
            add_vuln()
        elif c == "7":
            update_vuln()
        elif c == "8":
            delete_vuln()
        elif c == "0":
            sys.exit(0)
        else:
            print("Invalid option")


if __name__ == "__main__":
    main_menu()
