from packets.packet import Packet


class OfflinePing(Packet):
    packet_id = 0x01
    client_timestamp: int = None
    magic: bytes = None
    client_guid: int = None

    def decode_payload(self):
        self.client_timestamp = self.read_long()
        self.magic = self.read_magic()
        self.client_guid = self.read_long()
