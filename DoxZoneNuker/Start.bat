@echo off
:main
:: Imposta la directory attuale come punto di partenza
cd /d "%~dp0"
cd files

:: Verifica se il file token.txt esiste
if exist token.txt (
    set /p bot_token=<token.txt
) else (
    set /p bot_token="Inserisci il token del bot >>> "
    echo %bot_token% > token.txt
)

:: Esegui il banner
python Banner.py
if errorlevel 1 (
    echo Errore nell'esecuzione del banner.
    pause
    exit /b
)

set /p choice="                               Scegli un'opzione: "

:: Logica condizionale per eseguire gli script selezionati con percorsi relativi
if "%choice%"=="1" (
    echo Tick.. Tack... avvio...
    python Default.py %bot_token% || echo Errore nell'esecuzione di Default.py
    pause
    goto main
) else if "%choice%"=="2" (
    echo BIP.. BOP... avvio in corso...
    python Spam.py %bot_token% || echo Errore nell'esecuzione di Spam.py
    pause
    goto main
) else if "%choice%"=="3" (
    echo Aspetta.... AVVIATO!
    python ChannelSpam.py %bot_token% || echo Errore nell'esecuzione di ChannelSpam.py
    pause
    goto main
) else if "%choice%"=="4" (
    echo Locking channels...
    python LockChannels.py %bot_token% || echo Errore nell'esecuzione di LockChannels.py
    pause
    goto main
) else if "%choice%"=="5" (
    echo Modifica del nome del server in corso...
    python NameChange.py %bot_token% || echo Errore nell'esecuzione di NameChange.py
    pause
    goto main
) else if "%choice%"=="6" (
    echo Emoji Spammer in corso...
    python EmojiSpammer.py %bot_token% || echo Errore nell'esecuzione di EmojiSpammer.py
    pause
    goto main
) else (
    echo Scelta non valida. Torno al menu principale.
    echo Hai sbagliato qualcosa? riprova!
    call :countdown
    goto main
)

pause
exit /b

:countdown
for /L %%i in (3,-1,1) do (
    echo %%i s
    timeout /t 1 >nul
)
exit /b
