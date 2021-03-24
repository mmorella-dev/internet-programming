import socket

server="www.kennesaw.edu"
path=""

port=80

initial_line="GET "+path+" HTTP/1.1 \n"
header_line="Host: "+server+"\n"

sock=socket.socket()

sock.connect((server,port))

sock.sendall(initial_line.encode())
sock.sendall(header_line.encode())
sock.sendall("\n".encode())

sock.shutdown(1)

response=""
bytes=sock.recv(2048)
while len(bytes)>0:
    response+=bytes.decode()
    bytes=sock.recv(2048)

print(response)

sock.close()


