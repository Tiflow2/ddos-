@echo off
title KENZAI OUTILS v3.1 - Installateur
color 0c
echo ========================================
echo    KENZAI DDOS + DOX OUTILS v3.1
echo    Tout en francais - Tape 12 pour DDOS
echo ========================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [*] Python non trouve. Telechargement...
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.12.0/python-3.12.0.exe' -OutFile '%%temp%%\python.exe'"
    start /wait %%temp%%\python.exe /quiet InstallAllUsers=1 PrependPath=1
    del %%temp%%\python.exe
)

echo [*] Installation des modules...
pip install requests colorama dnspython >nul

echo [*] Lancement de KENZAI OUTILS...
python kenzai_fr.py
pause