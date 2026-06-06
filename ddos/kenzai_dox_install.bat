@echo off
title KENZAI DOX TOOLS v2.0 - Installer
color 0c
echo ========================================
echo    KENZAI DOX TOOLS v2.0
echo    Scan ultra-precis + GeoIP avancee
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
pip install requests colorama >nul

echo [*] Lancement...
python kenzai_dox.py
pause