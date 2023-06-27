from packets.packet import Packet


class NewIncomingConnection(Packet):
    packet_id = 0x13
    server_address: tuple = None
    internal_address: tuple = None

    def decode_payload(self):
        self.server_address = self.read_address()
        self.internal_address = self.read_address()
