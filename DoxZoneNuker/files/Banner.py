import os
import time

banner_lines = [
    "·▄▄▄▄        ▐▄• ▄ ·▄▄▄▄•       ▐ ▄ ▄▄▄ .     ▐ ▄ ▄• ▄▌▄ •▄ ▄▄▄ .▄▄▄  ",
    "██▪ ██ ▪      █▌█▌▪▪▀·.█▌▪     •█▌▐█▀▄.▀·    •█▌▐██▪██▌█▌▄▌▪▀▄.▀·▀▄ █·",
    "▐█· ▐█▌ ▄█▀▄  ·██· ▄█▀▀▀• ▄█▀▄ ▐█▐▐▌▐▀▀▪▄    ▐█▐▐▌█▌▐█▌▐▀▀▄·▐▀▀▪▄▐▀▀▄ ",
    "██. ██ ▐█▌.▐▌▪▐█·█▌█▌▪▄█▀▐█▌.▐▌██▐█▌▐█▄▄▌    ██▐█▌▐█▄█▌▐█.█▌▐█▄▄▌▐█•█▌",
    "▀▀▀▀▀•  ▀█▄▀▪•▀▀ ▀▀·▀▀▀ • ▀█▄▀▪▀▀ █▪ ▀▀▀     ▀▀ █▪ ▀▀▀ ·▀  ▀ ▀▀▀ .▀  ▀  by Sh1v3r"
]

colors = [
    "\033[38;2;255;0;0m",
    "\033[38;2;255;51;0m",
    "\033[38;2;255;102;0m",
    "\033[38;2;255;153;51m",
    "\033[38;2;255;200;100m"
]

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    for i, line in enumerate(banner_lines):
        color = colors[min(i, len(colors) - 1)]
        for char in line:
            print(color + char, end='', flush=True)
            time.sleep(0.015)
        print("\033[0m")
        time.sleep(0.05)

if __name__ == "__main__":
    print_banner()

