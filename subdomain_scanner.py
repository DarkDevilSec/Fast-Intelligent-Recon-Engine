#!/usr/bin/env python3

import subprocess
import sys
import os
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

def run_subfinder(domain):
    print("\033[94m[~] Trying Subfinder...\033[0m")
    result = subprocess.run(
        ["subfinder", "-d", domain, "-silent"],
        capture_output=True, text=True
    )
    return result.stdout.strip().split('\n')

def run_amass(domain):
    print("\033[94m[~] Trying Amass (passive mode)...\033[0m")
    result = subprocess.run(
        ["amass", "enum", "-d", domain, "-passive"],
        capture_output=True, text=True
    )
    return result.stdout.strip().split('\n')

def save_output(domain, subdomains):
    output_file = f"outputs/{domain}_subdomains.txt"
    os.makedirs("outputs", exist_ok=True)
    with open(output_file, "w") as f:
        for sub in subdomains:
            f.write(sub + "\n")
    return output_file

def main():
    banner()
    if len(sys.argv) != 2:
        print("\033[1m[x] Usage:\033[0m python3 subdomain_scanner.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    all_subs = []

    subs = run_subfinder(domain)
    subs = list(filter(None, subs))

    if not subs:
        subs = run_amass(domain)
        subs = list(filter(None, subs))

    if not subs:
        print("\033[93m[-] No subdomains found using Subfinder or Amass.\033[0m")
        return

    unique_subs = sorted(set(subs))
    file_path = save_output(domain, unique_subs)

    print(f"\n\033[92m[+] Found {len(unique_subs)} subdomains.\033[0m")
    print(f"\033[96m[✓] Saved to: {file_path}\033[0m\n")

    for sub in unique_subs:
        print(f" └─ {sub}")

if __name__ == "__main__":
    main()
