# 🔥 FIRE Recon - Fast Intelligent Reconnaissance Engine

```

🧠 **FIRE** stands for **Fast Intelligent Recon Engine** – a modular, OSINT-powered reconnaissance tool built for Red Teamers , Bug Bounty Hunters , and Security Analysts.

```
███████╗██╗██████╗ ███████╗    ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
██╔════╝██║██╔══██╗██╔════╝    ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
█████╗  ██║██████╔╝█████╗      ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
██╔══╝  ██║██╔══██╗██╔══╝      ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
██║     ██║██║  ██║███████╗    ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
```

🧪 Version: 1.0
🧑‍💻 Author: White Devil
🧭 OS: Kali Linux 2025.2
🎯 Focus: Web Recon, OSINT, Red Team

---

## ✨ Features

🔍 Basic Recon:
• 🌐 Site Title Fetch
• 📌 IP Address Resolution
• 🧭 GeoIP Lookup
• 🏷️ Web Server Detection
• 🤖 robots.txt Scanner

🛡️ Security Intel:
• ☁️ Cloudflare Detection
• 🧾 WHOIS Info
• 🛰️ Banner Grabbing
• 🌐 Subdomain Enumeration (Amass + Subfinder)
• 🚀 Nmap Scan (Top Ports + Services)
• 🧨 CVE Finder (based on open ports)

---

## ⚙️ Installation

🔧 Install Tools (Kali):

```bash
sudo apt install nmap amass subfinder whois curl -y
```

🐍 Install Python Dependencies:

```bash
pip3 install --break-system-packages -r requirements.txt
```

🧠 Auto Setup:

```bash
chmod +x setup.py
./setup.py
```

---

## 🚀 Usage

Start FIRE:

```bash
python3 fire.py
```

📋 Sample Menu:

```
[+] Site Title: example.com

Select Option:
 [1] IP Address
 [2] Web Server
 [3] Cloudflare Detection
 [4] Whois Lookup
 [5] Geo-IP Lookup
 [6] Robots.txt Scanner
 [7] Banner Grabbing
 [8] Subdomain Scanner
 [9] Nmap Port Scan
 [10] CVE Finder
 [99] Change Target
 [0] Exit
```


## 🖼️ Screenshot

![FIRE Recon Screenshot](https://raw.githubusercontent.com/WhiteDevil/FIRE-Recon/main/screenshot.png)

---

## 👑 Author

🧑 White Devil
🔗 LinkedIn: [https://www.linkedin.com/in/white-devil](https://www.linkedin.com/in/white-devil)
---

## ⚠️ Disclaimer

🔒 This tool is intended for **authorized testing** and **educational use only**.
Do not use against systems without **explicit permission**.
The creator is not responsible for any misuse or damage caused.

