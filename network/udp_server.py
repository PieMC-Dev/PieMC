import socket

class UDPServer:

    def __init__(self, hostname: str = "0.0.0.0", port: int = 19132):
        self.hostname = hostname
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.SOL_UDP)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.socket.bind((hostname, port))

    def recieve(self):
        return self.socket.recvfrom(65535)

    def send(self, data: bytes, address: tuple):
        self.socket.sendto(data, address)

    def close(self):
        self.socket.close()
