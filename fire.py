#!/usr/bin/env python3

import subprocess
import readline
import requests
from bs4 import BeautifulSoup

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
    print("📦  Version : 1.0   |   ⚔️  Linux Compatible")
    print("👑  Author  : Ashish Prajapati")
    print("🌐  GitHub  : https://github.com/DarkDevilSec/Fast-Intelligent-Recon-Engine")
    print("🧠  Web Recon Framework for Red Teamers & OSINT Experts")
    print("\033[0m")  # Reset color



def show_menu():
    print("\n\033[1mSelect Option:\033[0m")
    print(" [1] IP Address")
    print(" [2] Web Server")
    print(" [3] Cloudflare Detection")
    print(" [4] Whois Lookup")
    print(" [5] Geo-IP Lookup")
    print(" [6] Robots.txt Scanner")
    print(" [7] Banner Grabbing")
    print(" [8] Subdomain Enumeration")
    print(" [9] Nmap Scan")
    print(" [10] CVE Finder")
    print(" [99] Change Target")
    print(" [0] Exit")

def get_site_title(domain):
    try:
        print(f"\033[94m[~] Trying HTTP...\033[0m")
        res = requests.get(f"http://{domain}", timeout=5)
    except Exception:
        try:
            print("\033[93m[!] HTTP failed. Trying HTTPS...\033[0m")
            res = requests.get(f"https://{domain}", timeout=5, verify=False)
        except Exception as e:
            print(f"\033[91m[x] Title Error:\033[0m {e}")
            return

    try:
        soup = BeautifulSoup(res.text, 'html.parser')
        title = soup.title.string.strip() if soup.title else "No title found"
        print(f"\033[1m[+] Site Title:\033[0m {title}")
    except Exception as e:
        print(f"\033[91m[x] Parsing Error:\033[0m {e}")


def main():
    try:
        banner()
        target = ""
        while not target:
            target = input("\033[1m[>] Enter Target Domain:\033[0m ").strip()
        print()

        print("\033[1m[+] Site Title:\033[0m")
        get_site_title(target)

        while True:
            show_menu()
            choice = input("\n\033[1m[>] Enter your choice:\033[0m ").strip()

            if choice == "1":
                subprocess.run(["python3", "ip_resolver.py", target], check=False)
            elif choice == "2":
                subprocess.run(["python3", "web_server.py", target], check=False)
            elif choice == "3":
                subprocess.run(["python3", "cloudflare_check.py", target], check=False)
            elif choice == "4":
                subprocess.run(["python3", "whois_lookup.py", target], check=False)
            elif choice == "5":
                subprocess.run(["python3", "geoip_lookup.py", target], check=False)
            elif choice == "6":
                subprocess.run(["python3", "robots_scanner.py", target], check=False)
            elif choice == "7":
                subprocess.run(["python3", "banner_grabber.py", target], check=False)
            elif choice == "8":
                subprocess.run(["python3", "subdomain_scanner.py", target], check=False)
            elif choice == "9":
                subprocess.run(["python3", "nmap_scan.py", target], check=False)
            elif choice == "10":
                subprocess.run(["python3", "cve_finder.py", target], check=False)
            elif choice == "99":
                target = input("\033[1m[>] Enter NEW Target Domain:\033[0m ").strip()
                print("\033[1m[+] Site Title:\033[0m")
                get_site_title(target)
            elif choice == "0":
                print("\n\033[1m[!] Exiting FIRE. Stay 🔥, White Devil!\033[0m")
                break
            else:
                print("\033[1m[x] Invalid choice. Try again.\033[0m")

    except KeyboardInterrupt:
        print("\n\n\033[1m[!] Interrupted. Stay sharp, White Devil!\033[0m")
        exit()

if __name__ == "__main__":
    main()
