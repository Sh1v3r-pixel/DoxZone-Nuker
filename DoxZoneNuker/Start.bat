@echo off
cd files

:: Esegui solo il banner in Python
python C:\Users\Utente\Desktop\DoxZoneNuker\files\Banner.py
if errorlevel 1 (
    echo Errore nell'esecuzione del banner.
    pause
    exit /b
)

:main

:: Sezione del menu con effetto cromatico rosso per le linee e arancione elettrico per le opzioni
echo.
echo.
powershell -Command "Write-Host '                              ======================================================' -ForegroundColor DarkRed"
powershell -Command "Write-Host '                                          Discord: .gg/BZ3Qu9sjRe' -ForegroundColor DarkRed"
powershell -Command "Write-Host '                              ======================================================' -ForegroundColor DarkRed"
echo.

:: Opzioni di selezione con arancione elettrico
powershell -Command "Write-Host '                                               1)  Nuke Default' -ForegroundColor Yellow"
powershell -Command "Write-Host '                                               2)  Spammer' -ForegroundColor Yellow"
powershell -Command "Write-Host '                                               3)  Channel Spammer' -ForegroundColor Yellow"
powershell -Command "Write-Host '                                               4)  Lock Channels' -ForegroundColor Yellow"
powershell -Command "Write-Host '                                               5)  Name Change' -ForegroundColor Yellow"
powershell -Command "Write-Host '                                               6)  Emoji Spammer' -ForegroundColor Yellow"
echo.

powershell -Command "Write-Host '                              ======================================================' -ForegroundColor DarkRed"
echo.

:: Ricevi la scelta dell'utente
set /p choice="                               [\>] "

:: Logica condizionale per eseguire gli script selezionati
if "%choice%"=="1" (
    echo Tick.. Tack... avvio...
    python C:\Users\Utente\Desktop\DoxZoneNuker\files\Default.py || echo Errore nell'esecuzione di Default.py
    pause
    goto main
) else if "%choice%"=="2" (
    echo BIP.. BOP... avvio in corso...
    python C:\Users\Utente\Desktop\DoxZoneNuker\files\Spam.py || echo Errore nell'esecuzione di Spam.py
    pause
    goto main
) else if "%choice%"=="3" (
    echo Aspetta.... AVVIATO!
    python C:\Users\Utente\Desktop\DoxZoneNuker\files\ChannelSpam.py || echo Errore nell'esecuzione di ChannelSpam.py
    pause
    goto main
) else if "%choice%"=="4" (
    echo Locking channels...
    python C:\Users\Utente\Desktop\DoxZoneNuker\files\LockChannels.py || echo Errore nell'esecuzione di LockChannels.py
    pause
    goto main
) else if "%choice%"=="5" (
    echo Modifica del nome del server in corso...
    python C:\Users\Utente\Desktop\DoxZoneNuker\files\NameChange.py || echo Errore nell'esecuzione di NameChange.py
    pause
    goto main
) else if "%choice%"=="6" (
    echo Emoji Spammer in corso...
    python C:\Users\Utente\Desktop\DoxZoneNuker\files\EmojiSpammer.py || echo Errore nell'esecuzione di EmojiSpammer.py
    pause
    goto main
) else (
    echo Scelta non valida. Torno al menu principale.
    pause
    goto main
)

pause
exit /b
