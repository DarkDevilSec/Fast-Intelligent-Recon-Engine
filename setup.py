#!/usr/bin/env python3

import os
import subprocess
import shutil
import sys

cli_tools = [
    "nmap",
    "amass",
    "subfinder",
    "whois",
    "curl",
]

python_packages = [
    "wheel",  # 🛠 Fix for building binary packages
    "requests",
    "beautifulsoup4",
    "readline; platform_system == 'Linux'",
    "python-whois"
]

def check_tool(tool):
    return shutil.which(tool) is not None

def install_kali_tools():
    print("\n\033[1;96m[+] Checking and Installing CLI Tools:\033[0m\n")
    for tool in cli_tools:
        if not check_tool(tool):
            print(f"\033[93m[~] Installing {tool}...\033[0m")
            subprocess.run(["sudo", "apt", "install", "-y", tool], check=False)
        else:
            print(f"\033[92m[✓] {tool} already installed.\033[0m")

def install_python_packages():
    print("\n\033[1;96m[+] Installing Python Libraries:\033[0m\n")
    for pkg in python_packages:
        try:
            print(f"\033[93m[~] Installing {pkg}...\033[0m")
            subprocess.run(["pip3", "install", "--break-system-packages", pkg], check=False)
        except Exception as e:
            print(f"\033[91m[x] Failed to install {pkg}: {e}\033[0m")

def main():
    print("\n\033[1;91m🔥 FIRE Recon Installer 🔥\033[0m")
    print("🚀 Starting Installation...\n")

    install_kali_tools()
    install_python_packages()

    print("\n\033[1;92m[✓] All dependencies installed. FIRE is ready!\033[0m")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[91m[!] Installation aborted by user.\033[0m")
        sys.exit(1)
