from rich.console import Console
from rich import print
from rich.panel import Panel
import os
import time
import pyfiglet
import requests
import random

# Session-----Conslone-----INSTALL....
ses = requests.Session()
console = Console()

#-----package  TARMUX -----#
packages = [
    "termux-setup-storage", "pkg update", "pkg upgrade", "pkg install python", "pkg install python2",
    "pkg install python3", "pkg install python-pip", "pkg install wget", "pkg install fish", "pkg install ruby",
    "pkg install help", "pkg install git", "pkg install dnsutils", "pkg install php", "pkg install perl", 
    "pkg install lua", "pkg install parallel", "pkg install nmap", "pkg install bash", "pkg install clang",
    "pkg install nano", "pkg install w3m", "pkg install hydra", "pkg install figlet", "pkg install cowsay", 
    "pkg install curl", "pkg install tar", "pkg install zip", "pkg install unzip", "pkg install net-tools",
    "pkg install tor", "pkg install sudo", "pkg install wireshark", "pkg install wgetrc", "pkg install wcalc", 
    "pkg install openssl", "pkg install openssl-tool", "pkg install bmon", "pkg install vpn", "pkg install unrar",
    "pkg install toilet", "pkg install proot", "pkg install vim", "pkg install vim-python", "pkg install ired", 
    "pkg install goaccess", "pkg install golang", "pkg install kibi", "pkg install tsu", "pkg install tmux", 
    "pkg install mtools", "pkg install file", "pkg install pass", "pkg install pick", "pkg install chroot", 
    "termux-chroot", "pkg install macchanger", "pkg install ninja", "pkg install elixir", "pkg install swift", 
    "pkg install xmlstarlet", "pkg install fakeroot", "pkg install texinfo", "pkg install netcat", "pkg install wren", 
    "pkg install gatling", "pkg install cvs", "pkg install ffmpeg", "pkg install screen", "pkg install neofetch", 
    "pkg install mariadb", "pkg install picolisp", "pkg install cmatrix", "pkg install dropbear", "pkg install openssh", 
    "pkg install python-pip", "pip2 install wget", "pip install bs4", "pip2 install bs4", "pip install requests", 
    "pip2 install requests", "pip install mechanize", "pip2 install mechanize", "pip install php", "pip2 install php"
]

#--------Colour CODE------#
A = "\x1b[38;5;28m"
B = "\x1b[38;5;50m"
C = "\x1b[38;5;105m"
D = "\x1b[38;5;46m"
E = "\x1b[38;5;15m"
F = "\x1b[38;5;265m"
G = "\x1b[38;5;226m"
I = "\x1b[38;5;123m"
J = "\x1b[38;5;160m"
K = "\x1b[38;5;81m"
L = "\x1b[1;34m"

#-----------------------#EMOJI system-------#
X = "[漏]"
V = """
     "[bold green]馃挌[/] [bold yellow]馃挴[/] [bold red]鉂わ笍鈥嶐煩筟/] "
    "[bold magenta]馃ぉ[/] [bold orange]馃А[/] [bold blue]馃挋[/] "
    "[bold purple]馃挏[/] [bold cyan]馃拵[/] [bold white]馃専[/] "
    "[bold bright_red]馃嚥馃嚞[/] [bold bright_yellow]馃寛[/] "
"""
#--------def clear --------#
def clear():
    print("Jone MY Whatsapp Groupe MALAGASY馃挌馃挌馃専馃専")
    os.system('espeak -a 100 " jone,MY Whatsapp Groupe MALAGASY "')
    os.system("xdg-open https://t.me/KGF_CYBER_TEM")
    os.system("xdg-open https://t.me/KGF_CYBER_TEM")
    print(" install modeul just waint...FUCK YOU NOT WAINT馃ぃ馃ぃ馃槀 ")
    os.system('espeak -a 100 " install ,  module just white MARC TOOL"')
    os.system("pip install rich pyfiglet requests")
    os.system('pkg install espeak')
    os.system('clear')

#----------LOGO------KALYAN------#
logo_text = "SETUP TERMUX BY JEAN MARC MALAGASY TOOL"
ascii_logo = pyfiglet.figlet_format(logo_text)

def speak(message):
    os.system(f'espeak -a 100 "{message}"')

#------------MENU MAIN
def main():
    clear()
    print(f"[bold cyan]{ascii_logo}[/bold cyan]")
    console.print("[bold bright_blue]DEVELOPER :[/] [bold green]JEAN MARC[/] [yellow]鈥⑩�/]")
    console.print("[bold green] TOOL : TARMUX SETUP[/] [yellow]鈽呪槄[/]")
    console.print("[bold green] WHATSAPP : https://wa.me/qr/KL5PP6QUQ66LM1[/] [yellow]鈫掆啋鈽匸/]")
    console.print("[bold green] VERSION : 0.1[/] [yellow]鈥嶁墵鈮圼/]")
    console.print(V)
    
    speak("Welcome to Tarmux setup. Choose an option.")
    console.print(f"[bold green]1.[/bold green] [cyan]TERMUX SETUP[/cyan]")
    console.print(f"[bold green]2.[/bold green] [magenta]OWNER CALL[/magenta]")
    option = input(f"{X} CHOICE : ")
    
    if option == "1":
        speak("Starting Termux setup.")
        mix_x()
    elif option == "2":
        speak("Calling owner feature coming soon!")
        console.print(f"[yellow]Calling Owner...[/yellow] [cyan](Feature coming soon!)[/cyan]")
        os.system("xdg-open https://wa.me/qr/KL5PP6QUQ66LM1")
        time.sleep(2)
    else:
        speak("Please select a correct option.")
        print(f"{J}{X} PLEASE SELECT CORRECTLY !!")
        time.sleep(2)
        main()

def mix_x():
    clear()
    for package in packages:  # LOOP------INSTALLl----PACES
        speak(f"Installing {package}")
        print(f"[bold cyan]{ascii_logo}[/bold cyan]")
        print(f"[bold cyan]Installing {package}...[/bold cyan]")
        os.system(package)
        
        #EMOJI______INSTALL-------#
        print(f"[bold green]鉁� {package} installed successfully![/bold green] {random.choice(['馃敟', '馃挴', '馃帀', '馃専','馃嚥馃嚞'])}")
        time.sleep(1)  # 1-----Packeecs download of review emjoi-------#
    
    speak("All packages installed successfully!")
    print("[bold green]All packages installed successfully![/bold green] 馃帀馃嚥馃嚞馃帀")
    time.sleep(2)
    main()

main()
