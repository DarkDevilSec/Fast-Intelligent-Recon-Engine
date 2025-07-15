#!/usr/bin/env python3

import sys
import requests
import socket
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

def clean_target(target):
    # Remove URL schemes and paths
    target = target.replace("https://", "").replace("http://", "").split("/")[0]
    return target

def resolve_to_ip(target):
    try:
        return socket.gethostbyname(target)
    except Exception:
        return target  # May already be IP

def geoip_lookup(ip):
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data = res.json()

        if data['status'] == 'success':
            print(f"\033[1m[+] IP:\033[0m {data['query']}")
            print(f"\033[1m[+] Country:\033[0m {data['country']} ({data['countryCode']})")
            print(f"\033[1m[+] Region:\033[0m {data['regionName']}")
            print(f"\033[1m[+] City:\033[0m {data['city']}")
            print(f"\033[1m[+] ISP:\033[0m {data['isp']}")
            print(f"\033[1m[+] Org:\033[0m {data['org']}")
            print(f"\033[1m[+] AS:\033[0m {data['as']}")
            print(f"\033[1m[+] Timezone:\033[0m {data['timezone']}")
            print(f"\033[1m[+] Coordinates:\033[0m {data['lat']}, {data['lon']}")
        else:
            print(f"\033[1m[x] GeoIP Error:\033[0m {data.get('message', 'Unknown Error')}")
    except Exception as e:
        print(f"\033[1m[x] Request Error:\033[0m {e}")

def main():
    banner()
    if len(sys.argv) > 1:
        raw_target = sys.argv[1]
    else:
        raw_target = input("\033[1m[>] Enter Target Domain or IP:\033[0m ").strip()

    clean = clean_target(raw_target)
    ip = resolve_to_ip(clean)

    print(f"\n\033[1m[~] Looking up:\033[0m {ip}\n")
    geoip_lookup(ip)

if __name__ == "__main__":
    main()
