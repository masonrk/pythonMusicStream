# mason kelly
# cs447
import socket
import sys
import random
import time
serverPort = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) < 4:
    print("Missing port # or Host name")
    hostName = input("please enter the host name: ")
    serverPort = input("Please enter port number: ")
if len(sys.argv) > 4:
    print("Too many arguments provided")
    print("first and second argument will be used")
if len(sys.argv) == 4:
    hostName = sys.argv[1]
    serverPort = sys.argv[2]
    recieverPort = sys.argv[3]
serverPort = int(serverPort)
data = "0"
lvl = 0
mini = 0
maxi = 2 ** 8
seq = random.randint(mini, maxi)
serverName = socket.gethostbyname(hostName)
server_address = (hostName, serverPort)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)
print("connected")
message = ''
keyIn = ""
while keyIn.upper() != 'TEARDOWN':
    if lvl == 0:
        message = str(seq) + " portNumber " + str(recieverPort)
        message = message.encode()
        sock.sendall(message)
        lvl = 1
        seq + 1
    keyIn = input()
    message = " " + keyIn
    message = str(seq) + message +" "
    message = message.encode()
    print('\nsending "%s"' % message)
    count = 0

    while int(data.split()[0]) != seq:
        sock.sendall(message)

        if keyIn.upper() == "TEARDOWN":
            break
        if count == 0:
            print("sent")
            print("CSeq:  %d \n" % seq)
        amount = 0

        while amount == 0:
            data = sock.recv(200)
            data = data.decode()
            amount = len(data)
            print('recieved "%s"' % data)
    seq = seq + 1
    message = message.decode()
    message = message.split()[0]
print('closing socket')
time.sleep(3)
sock.close()
