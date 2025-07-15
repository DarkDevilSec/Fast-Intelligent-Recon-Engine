#!/usr/bin/env python3

import sys
import whois
import readline  # For arrow key recall

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

def format_field(field):
    try:
        if isinstance(field, list):
            return str(field[0])  # Take the first item if it's a list
        elif field:
            return str(field)
        else:
            return "N/A"
    except:
        return "N/A"

def whois_lookup(domain):
    try:
        data = whois.whois(domain)

        print(f"\033[1m[+] Domain:\033[0m {domain}")
        print(f"\033[1m[+] Registrar:\033[0m {format_field(data.registrar)}")
        print(f"\033[1m[+] Whois Server:\033[0m {format_field(data.whois_server)}")
        print(f"\033[1m[+] Name Servers:\033[0m {format_field(data.name_servers)}")
        print(f"\033[1m[+] Domain Status:\033[0m {format_field(data.status)}")
        print(f"\033[1m[+] Org:\033[0m {format_field(data.org)}")
        print(f"\033[1m[+] Country:\033[0m {format_field(data.country)}")
        print(f"\033[1m[+] Creation Date:\033[0m {format_field(data.creation_date)}")
        print(f"\033[1m[+] Updated Date:\033[0m {format_field(data.updated_date)}")
        print(f"\033[1m[+] Expiration Date:\033[0m {format_field(data.expiration_date)}")
        print(f"\033[1m[+] DNSSEC:\033[0m {format_field(data.dnssec)}")
        print(f"\033[1m[+] Emails:\033[0m {format_field(data.emails)}")

    except Exception as e:
        print(f"\033[1m[x] Whois Lookup Error:\033[0m {e}")

def main():
    banner()
    
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = input("\033[1m[>] Enter Target Domain:\033[0m ").strip()

    print()
    whois_lookup(target)

if __name__ == "__main__":
    main()
