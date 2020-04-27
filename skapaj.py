import socket
import select
import sys
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print "Zadaj: script, IP address, port number"
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
nickname = raw_input('nickname: ')
server.connect((IP_address, Port))
server.send(nickname)

cls()

while True:
    sockets_list = [sys.stdin, server]
    read_sockets,write_socket, error_socket = select.select(sockets_list, [], [])
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            print message
        else:
            message = sys.stdin.readline()
            print ""
            server.send(message)
            sys.stdout.flush()
server.close()