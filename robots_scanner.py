#!/usr/bin/env python3

import sys
import requests
import readline

def banner():
    print("\033[1;91m")  # Red Bold
    print("███████╗██╗██████╗ ███████╗    ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗")
    print("██╔════╝██║██╔══██╗██╔════╝    ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║")
    print("█████╗  ██║██████╔╝█████╗      ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║")
    print("██╔══╝  ██║██╔══██╗██╔══╝      ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║")
    print("██║     ██║██║  ██║███████╗    ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║")
    print("╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝")
    print("\033[1;93m")  # Yellow bold for info
    print("🔥  FIRE Recon - Fast Intelligent Reconnaissance Engine")
    print("📦  Version : 1.0   |   ⚔️  Kali Linux 2025.2 Compatible")
    print("👑  Author  : Ashish Prajapati")
    print("🌐  GitHub  : https://github.com/ashish143-hacker/Fast-Intelligent-Recon-Engine.git")
    print("🧠  Web Recon Framework for Red Teamers & OSINT Experts")
    print("\033[0m")  # Reset color

def fetch_robots(domain, debug=False):
    urls = [f"https://{domain}/robots.txt", f"http://{domain}/robots.txt"]
    for url in urls:
        try:
            if debug:
                print(f"\033[94m[*] Trying:\033[0m {url}")
            res = requests.get(url, timeout=5)
            if res.status_code == 200 and "html" not in res.headers.get("Content-Type", ""):
                print(f"\033[1m[+] robots.txt found at:\033[0m {url}\n")
                for line in res.text.splitlines():
                    if line.strip():
                        if line.lower().startswith("disallow"):
                            print(f"\033[91m{line}\033[0m")
                        elif line.strip().startswith("#"):
                            print(f"\033[90m{line}\033[0m")
                        else:
                            print(line)
                return
            else:
                if debug:
                    print(f"\033[93m[-] {url} responded with status {res.status_code}\033[0m")
        except requests.exceptions.RequestException as e:
            if debug:
                print(f"\033[91m[x] Error accessing {url}:\033[0m {e}")
            continue

    print("\033[1m[x] robots.txt not found or blocked.\033[0m")

def main():
    banner()

    if len(sys.argv) > 1:
        domain = sys.argv[1]
    else:
        domain = input("\033[1m[>] Enter Target Domain:\033[0m ").strip()

    print()
    fetch_robots(domain, debug=False)  # Set to True for debug output

if __name__ == "__main__":
    main()
