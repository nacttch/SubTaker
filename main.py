#!/usr/bin/env python3
import socket
import json
import os
import sys
import time
from utils import print_banner, colored

def resolve_subdomain(domain, sub):
    try:
        target = f"{sub}.{domain}"
        ip = socket.gethostbyname(target)
        return {"subdomain": target, "ip": ip, "resolved": True}
    except Exception:
        return {"subdomain": f"{sub}.{domain}", "ip": None, "resolved": False}

def run(domain, mode, filepath=None):
    results = []
    subs = []

    if mode == "1":
        sub = input(colored("[?] Enter a subdomain (without domain): ", "cyan"))
        subs = [sub]
    elif mode == "2":
        if not filepath or not os.path.exists(filepath):
            print(colored("[!] Invalid file path", "red"))
            return []
        with open(filepath) as f:
            subs = [line.strip() for line in f if line.strip()]
    elif mode == "3":
        default_file = os.path.join(os.path.dirname(__file__), "subdomains.txt")
        with open(default_file) as f:
            subs = [line.strip() for line in f if line.strip()]
    else:
        print(colored("[!] Invalid option", "red"))
        return []

    print(colored(f"[+] Checking {len(subs)} subdomains...", "yellow"))
    for sub in subs:
        res = resolve_subdomain(domain, sub)
        results.append(res)
        status = colored("LIVE", "green") if res["resolved"] else colored("DEAD", "red")
        print(f" - {res['subdomain']} -> {res['ip']} [{status}]")
        time.sleep(0.2)

    out_file = os.path.join(os.path.dirname(__file__), "report.json")
    with open(out_file, "w") as f:
        json.dump(results, f, indent=2)
    print(colored(f"[+] Report saved to {out_file}", "cyan"))
    return results

if __name__ == "__main__":
    print_banner()
    domain = input(colored("[?] Enter target domain (example.com): ", "cyan")).strip()
    if not domain:
        print(colored("[!] No domain provided", "red"))
        sys.exit(1)

    print("""
Choose mode:
 [1] Single subdomain input
 [2] Use custom file path
 [3] Use default wordlist (subdomains.txt)
 [4] Exit
""")
    choice = input(colored("Enter choice: ", "cyan")).strip()
    if choice == "4":
        print(colored("[*] Exiting...", "yellow"))
        sys.exit(0)
    elif choice in ["1","2","3"]:
        filepath = None
        if choice == "2":
            filepath = input(colored("[?] Enter path to subdomain wordlist: ", "cyan")).strip()
        run(domain, choice, filepath)
    else:
        print(colored("[!] Invalid choice", "red"))
        sys.exit(1)
