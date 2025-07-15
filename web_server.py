#!/usr/bin/env python3

import requests
import sys
import readline  # Enables arrow key recall in terminal

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

def detect_web_server(domain):
    try:
        response = requests.get(f"http://{domain}", timeout=5)
        server = response.headers.get('Server', 'Header not found')
        print(f"\033[1m[+] Web Server:\033[0m {server}")
    except requests.exceptions.RequestException as e:
        print(f"\033[1m[x] Web Server Detection Error:\033[0m {e}")

def main():
    banner()
    
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = input("\033[1m[>] Enter Target Domain:\033[0m ").strip()

    print()
    detect_web_server(target)

if __name__ == "__main__":
    main()
