class Connection:

    def __init__(self, server, address: tuple, mtu_size: int):
        self.server = server
        self.address = address
        self.mtu_size = mtu_size # idk
        self.active = False 
        self.ping = 0 # ms
        self.packets = [] # non-handled packets

    def send(self, data):
        self.server.socket.sendto(data, self.address)

    def disconnect(self):
        pass # wip
