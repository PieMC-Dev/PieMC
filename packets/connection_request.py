from packets.packet import Packet


class ConnectionRequest(Packet):
    packet_id = 0x09
    guid: int = None
    time: int = None
    
    def decode_payload(self):
        self.read_long(self.guid)
        self.read_long(self.time)