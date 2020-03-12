import socket

srv_addr = input("Type the server IP address: ")
srv_port = int(input("Type the server port: "))
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((srv_addr, srv_port))
soc.listen(1)
print("Server started!!!")
connection, address = soc.accept()
print("Client connected with address:", address)
while 1:
    data = connection.recv(1024)
    if not data:
        break
    connection.sendall(b'-- Message Received --\n')
    print(data.decode('utf-8'))
connection.close()
