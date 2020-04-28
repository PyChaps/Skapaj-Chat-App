import socket
import select
import os
import sys 
from termcolor import colored, cprint
import skapaj_logo

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

skapaj_logo.skapaj_text()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print("Zadaj: script, IP address, port number")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
nickname = input(colored('Nickname: ', 'yellow'))
server.connect((IP_address, Port))
server.send(nickname.encode())
counter = 0

cls()

while True:
    sockets_list = [sys.stdin, server]
    read_sockets,write_socket, error_socket = select.select(sockets_list, [], [])
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            counter += 1
            if counter == 1:
                print(colored(message.decode(), 'green'))
                print("")
            else:
                print(colored(message.decode(), 'red'))
        else:
            message = sys.stdin.readline()
            print("")
            server.send(message.encode())
            sys.stdout.flush()
server.close()