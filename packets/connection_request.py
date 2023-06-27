from packets.packet import Packet


class ConnectionRequest(Packet):
    packet_id = 0x09
    client_guid: int = None
    client_timestamp: int = None
    
    def decode_payload(self):
        self.client_guid = self.read_long()
        self.client_timestamp = self.read_long()