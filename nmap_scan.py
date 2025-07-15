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

def run_nmap(domain, detect_os=False):
    os.makedirs("outputs", exist_ok=True)
    output_file = f"outputs/{domain}_nmap.txt"

    print("\n\033[1;94m[~] Scanning ports with version detection...\033[0m")

    cmd = ["nmap", "-sV", domain, "-oN", output_file]

    if detect_os:
        print("\033[94m[~] Enabling OS detection (-O)...\033[0m")
        cmd.insert(1, "-O")

    try:
        subprocess.run(cmd, check=True)
        print(f"\n\033[92m[✓] Scan complete. Saved to {output_file}\033[0m\n")

        # Print summary from file
        with open(output_file) as f:
            lines = f.readlines()
            for line in lines:
                if line.strip():
                    print(" " + line.strip())

    except Exception as e:
        print(f"\033[91m[x] Error running nmap:\033[0m {e}")

def main():
    banner()

    if len(sys.argv) != 2:
        print("\033[91m[x] Usage:\033[0m python3 nmap_scan.py <target>")
        sys.exit(1)

    target = sys.argv[1]

    detect = input("\033[1m[?] Enable OS Detection (Y/N)?\033[0m ").strip().lower()
    run_nmap(target, detect_os=(detect == 'y'))

if __name__ == "__main__":
    main()
