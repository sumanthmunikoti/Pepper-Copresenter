import socket
import sys
from naoqi import ALProxy

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

sock.listen(1)

while True:
    print >> sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >> sys.stderr, 'connection from', client_address
        tts = ALProxy("ALAnimatedSpeech", "192.168.1.3", 9559)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            tts.say(data)
            print >> sys.stderr, 'received "%s"' % data
            if data:
                print >> sys.stderr, 'do nothing'
                # connection.sendall(data)
            else:
                print >> sys.stderr, 'no more data from', client_address
                break

    finally:
        # Clean up the connection
        print ("Not closing the connection")
        # connection.close()