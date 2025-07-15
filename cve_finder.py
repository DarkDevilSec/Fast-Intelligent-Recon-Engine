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

def run_vuln_scan(target):
    os.makedirs("outputs", exist_ok=True)
    output_file = f"outputs/{target}_cves.txt"

    print(f"\n\033[94m[~] Running Nmap vuln scan on {target}...\033[0m\n")

    try:
        result = subprocess.run(
            ["nmap", "-sV", "--script", "vuln", target],
            capture_output=True,
            text=True
        )

        output = result.stdout
        with open(output_file, "w") as f:
            f.write(output)

        print(f"\033[92m[✓] Scan complete. Saved to {output_file}\033[0m\n")

        # Print lines with CVEs or vulnerabilities
        for line in output.splitlines():
            if "CVE" in line or "VULNERABLE:" in line:
                print(f"\033[91m{line}\033[0m")
            elif "State:" in line:
                print(f"\033[93m{line}\033[0m")

    except Exception as e:
        print(f"\033[91m[x] Error running vuln scan:\033[0m {e}")

def main():
    banner()

    if len(sys.argv) != 2:
        print("\033[91m[x] Usage:\033[0m python3 cve_finder.py <target>")
        sys.exit(1)

    target = sys.argv[1]
    run_vuln_scan(target)

if __name__ == "__main__":
    main()
