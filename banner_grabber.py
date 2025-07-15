#!/usr/bin/env python3

import socket
import sys
import readline

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 587, 3306, 8080]

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

def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(3)
        s.connect((ip, port))
        try:
            result = s.recv(1024).decode(errors='ignore').strip()
        except socket.timeout:
            result = "Timed out waiting for banner"
        s.close()
        return result if result else "No banner returned"
    except socket.timeout:
        return "Timeout: Host not responding"
    except ConnectionRefusedError:
        return "Connection refused"
    except Exception as e:
        return f"Error: {e}"

def resolve_domain(domain):
    try:
        return socket.gethostbyname(domain)
    except Exception as e:
        print(f"\033[1m[x] Error resolving domain:\033[0m {e}")
        sys.exit(1)

def main():
    banner()  # ✅ Fixed line

    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = input("\033[1m[>] Enter Target Domain or IP:\033[0m ").strip()

    ip = resolve_domain(target)
    print(f"\n\033[1m[~] Scanning {ip} on common ports...\033[0m\n")

    for port in COMMON_PORTS:
        banner_output = grab_banner(ip, port)
        if "No banner returned" in banner_output or "Timed out" in banner_output or "Connection refused" in banner_output:
            print(f"\033[90m[-] Port {port}: {banner_output}\033[0m")
        else:
            print(f"\033[92m[+] Port {port}:\033[0m {banner_output}")

if __name__ == "__main__":
    main()
