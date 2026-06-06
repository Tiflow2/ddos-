@echo off
title KENZAI DOX TOOLS - Installer
color 0c
echo ========================================
echo    KENZAI DOX TOOLS v1.0
echo    OSINT - Recherche d'informations
echo ========================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [*] Installation de Python...
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.12.0/python-3.12.0.exe' -OutFile '%%temp%%\python.exe'"
    start /wait %%temp%%\python.exe /quiet InstallAllUsers=1 PrependPath=1
    del %%temp%%\python.exe
)

echo [*] Installation des modules...
pip install requests colorama beautifulsoup4 phonenumbers dnspython >nul

echo [*] Lancement...
python kenzai_dox.py
pause