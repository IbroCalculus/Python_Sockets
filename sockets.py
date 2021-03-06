import socket
import time

'''
#CREATE A SOCKET.        NB: You need internet connection
sockObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockObject.connect(("www.google.com",80))
'''


#CREATE A SOCKET.        NB: You need internet connection
sockObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockObject.connect(('data.pr4e.org',80))        #NB: Remove http(s)

#Send command to receive data
command = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
sockObject.send(command)
print("Commmand sent")
time.sleep(3)
print("Receiving data in...")
for i in range(3,0,-1):
    print(i, end="\n")
    time.sleep(1)
time.sleep(1)

#Receive and parse data
while True:
    data = sockObject.recv(512)
    if(len(data) < 1):
        break
    print(data.decode())
sockObject.close()
