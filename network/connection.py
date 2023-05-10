from PieMC_Bedrock.protocol.packets.disconnect import Disconnect

class Connection:

    def __init__(self, server, address: tuple, mtu_size: int):
        self.server = server
        self.address = address
        self.mtu_size = mtu_size
        self.connected = False 
        self.ping = 0
        self.packets = []
        self.last_recieve_time = 0
        self.last_ping_time = 0
        self.guid = None

    def send(self, data):
        self.server.socket.sendto(data, self.address)

    def disconnect(self):
        packet = Disconnect()
        packet.encode()
        self.server.send(packet, self.address)
        self.server.remove_connection(self)
