from packets.packet import Packet


class OpenConnectionRequest2(Packet):
    packet_id = 0x07
    magic: bytes = None
    server_address: bytes = None
    mtu_size: int = None
    client_guid: int = None

    def decode_payload(self):
        self.magic = self.read_magic()
        self.read_address = self.read_ubyte()
        self.mtu_size = len(self.read_remaining())
        self.read_long(self.client_guid)
