import socket

name =  socket.gethostname()

add = socket.gethostbyname(name)

print(add,name)