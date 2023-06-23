from .packet import Packet


class OfflinePing(Packet):
    packet_id = 0x01
    client_timestamp = None
    magic = None
    client_guid = None

    def decode_payload(self):
        self.client_timestamp = self.read_long()
        self.magic = self.read_magic()
        self.client_guid = self.read_long()
