#!/usr/bin/env python3

import requests
import sys

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

def check_cloudflare(domain):
    try:
        res = requests.get(f"http://{domain}", timeout=5)
        headers = res.headers

        cf_indicators = ["cf-ray", "cf-cache-status", "cloudflare", "server: cloudflare"]
        detected = False

        print("\033[1m[+] Response Headers:\033[0m")
        for header, value in headers.items():
            line = f"{header}: {value}"
            print("   " + line)
            if any(indicator.lower() in line.lower() for indicator in cf_indicators):
                detected = True

        print()
        if detected:
            print("\033[1;92m[✔] Cloudflare protection is active.\033[0m")
        else:
            print("\033[1;91m[!] Cloudflare not detected in headers.\033[0m")
    except Exception as e:
        print(f"\033[1m[x] Error:\033[0m {e}")

def main():
    banner()
    
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = input("\033[1m[>] Enter Target Domain:\033[0m ").strip()

    print()
    check_cloudflare(target)

if __name__ == "__main__":
    main()
