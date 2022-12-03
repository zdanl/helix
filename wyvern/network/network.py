import socket

class Network:

    socket = None
    hostname = None
    port = None

    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect()

    def connect(self):
        self.socket.connect((self.hostname, self.port))

    def disconnect(self):
        self.socket.close()
