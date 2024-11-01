import os
import time

banner = """\
                       ·▄▄▄▄        ▐▄• ▄ ·▄▄▄▄•       ▐ ▄ ▄▄▄ .     ▐ ▄ ▄• ▄▌▄ •▄ ▄▄▄ .▄▄▄  
                       ██▪ ██ ▪      █▌█▌▪▪▀·.█▌▪     •█▌▐█▀▄.▀·    •█▌▐██▪██▌█▌▄▌▪▀▄.▀·▀▄ █·
                       ▐█· ▐█▌ ▄█▀▄  ·██· ▄█▀▀▀• ▄█▀▄ ▐█▐▐▌▐▀▀▪▄    ▐█▐▐▌█▌▐█▌▐▀▀▄·▐▀▀▪▄▐▀▀▄ 
                       ██. ██ ▐█▌.▐▌▪▐█·█▌█▌▪▄█▀▐█▌.▐▌██▐█▌▐█▄▄▌    ██▐█▌▐█▄█▌▐█.█▌▐█▄▄▌▐█•█▌
                       ▀▀▀▀▀•  ▀█▄▀▪•▀▀ ▀▀·▀▀▀ • ▀█▄▀▪▀▀ █▪ ▀▀▀     ▀▀ █▪ ▀▀▀ ·▀  ▀ ▀▀▀ .▀  ▀  v1.0 by Sh1v3r
"""

# Imposta il menu in rosso
menu = """\
\033[38;2;255;0;0m
                                             
                                             ╔═══                            ═══╗                                
                                             ║  ╔════════════════════════════╗  ║
                                                ║ [1] Nuke Default           ║
                                                ║ [2] Spammer                ║
                                                ║ [3] Channel Spammer        ║
                                                ║ [4] LockChannels           ║
                                                ║ [5] Name Change            ║
                                                ║ [6] Emoji Spammer          ║
                                                ║                            ║ 
                                             ║  ╚════════════════════════════╝  ║ 
                                             ╚═══                            ═══╝
  

\033[0m
"""

colors = [
    "\033[38;2;255;0;0m",
    "\033[38;2;255;51;0m",
    "\033[38;2;255;102;0m",
    "\033[38;2;255;153;51m",
    "\033[38;2;255;200;100m"
]

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    lines = banner.splitlines()
    for i, line in enumerate(lines):
        color = colors[min(i, len(colors) - 1)]
        for char in line:
            print(color + char, end='', flush=True)
            time.sleep(0.015)
        print("\033[0m")  # Reset colore
        time.sleep(0.05)

def show_menu():
    print(menu)
    choice = input("[\>] ")
    return choice

def main():
    print_banner()
    
    while True:
        choice = show_menu()
        
        if choice == "1":
            print("Tick.. Tack... avvio...")
            os.system("python Default.py")
        elif choice == "2":
            print("avvio in corso...")
            os.system("python Spam.py")
        elif choice == "3":
            print("Aspetta.... AVVIATO!")
            os.system("python ChannelSpam.py")
        elif choice == "4":
            print("Locking channels...")
            os.system("python LockChannels.py")
        elif choice == "5":
            print("Avviato!")
            os.system("python NameChange.py")
        elif choice == "6":
            print("Emoji Spammer in corso...")
            os.system("python EmojiSpammer.py")
        else:
            print("Scelta non valida. Torno al menu principale.")

if __name__ == "__main__":
    main()
