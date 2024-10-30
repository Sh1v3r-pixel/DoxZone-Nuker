@echo off
:: Imposta la directory attuale come punto di partenza
cd /d "%~dp0"
cd files

:: Esegui il banner
python Banner.py
if errorlevel 1 (
    echo Errore nell'esecuzione del banner.
    pause
    exit /b
)

:main

echo.
echo.
echo                              ======================================================
echo                                              Discord: .gg/BZ3Qu9sjRe
echo                              ======================================================
echo.
echo                                              1)  Nuke Default
echo                                              2)  Spammer
echo                                              3)  Channel Spammer
echo                                              4)  Lock Channels
echo                                              5)  Name Change
echo                                              6)  Emoji Spammer
echo.
echo                              ======================================================

:: Ricevi la scelta dell'utente
set /p choice="                               [\>] "

:: Logica condizionale per eseguire gli script selezionati con percorsi relativi
if "%choice%"=="1" (
    echo Tick.. Tack... avvio...
    python Default.py || echo Errore nell'esecuzione di Default.py
    pause
    goto main
) else if "%choice%"=="2" (
    echo BIP.. BOP... avvio in corso...
    python Spam.py || echo Errore nell'esecuzione di Spam.py
    pause
    goto main
) else if "%choice%"=="3" (
    echo Aspetta.... AVVIATO!
    python ChannelSpam.py || echo Errore nell'esecuzione di ChannelSpam.py
    pause
    goto main
) else if "%choice%"=="4" (
    echo Locking channels...
    python LockChannels.py || echo Errore nell'esecuzione di LockChannels.py
    pause
    goto main
) else if "%choice%"=="5" (
    echo Modifica del nome del server in corso...
    python NameChange.py || echo Errore nell'esecuzione di NameChange.py
    pause
    goto main
) else if "%choice%"=="6" (
    echo Emoji Spammer in corso...
    python EmojiSpammer.py || echo Errore nell'esecuzione di EmojiSpammer.py
    pause
    goto main
) else (
    echo Scelta non valida. Torno al menu principale.
    pause
    goto main
)

pause
exit /b
