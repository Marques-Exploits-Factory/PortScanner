import colorama 
from colorama import Fore
import os
import socket
import time

class Startup:
    
    def __init__(self): 
        pass
    
    def main(self):
        os.system("cls")
        print(f"""

{Fore.MAGENTA}
         ____            _   ____                                  
        |  _ \ ___  _ __| |_/ ___|  ___ __ _ _ __  _ __   ___ _ __ 
        | |_) / _ \| '__| __\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
        |  __/ (_) | |  | |_ ___) | (_| (_| | | | | | | |  __/ |   
        |_|   \___/|_|   \__|____/ \___\__,_|_| |_|_| |_|\___|_|   {Fore.RESET}

                                    {Fore.BLUE}Created by {Fore.MAGENTA}Gustavo Marques{Fore.BLUE}, from Marques-Exploits-Factory{Fore.RESET}

   {Fore.BLUE}           
            [1] PortScanner
            [2] Information
            [3] Exit{Fore.RESET}
""")
        choice = input(f"{Fore.GREEN}Select your choice > {Fore.RESET}") # Input for choice
        
        if choice == "1":
            
            ondeconectar = input(f"{Fore.MAGENTA}Adress: {Fore.RESET}")
            portas = [22, 24, 21, 443, 80, 465, 587, 989, 990, 554]

            for porta in portas:
                cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                cliente.settimeout(0.1)
                codigo = cliente.connect_ex((ondeconectar, porta))
            
            
                print(f"                                          {Fore.GREEN}CONNECTED TO:                                                 ")
                print(f"{Fore.MAGENTA}==========================================================================================================")
                print(cliente)
                print(f"{Fore.MAGENTA}==========================================================================================================")
                print(f"laddr=Orign    |    raddr=Target{Fore.YELLOW}")

                if codigo == 0:
                    print(codigo)
                    print(f"{Fore.GREEN}Connection successful{Fore.RESET}")
                else:
                    print(codigo)
                    print(f"{Fore.MAGENTA}Connection denied")   

                time.sleep(10)

        else:
            self.main()
       
        if choice == "3":
            print("Thanks for using PortScanner. Follow Marques-Exploits-Factory on github")
            
            time.sleep(10)
        else:
            self.main()

s = Startup()
s.main()