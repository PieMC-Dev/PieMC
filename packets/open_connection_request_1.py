from packets.packet import Packet


class OpenConnectionRequest1(Packet):
    packet_id = 0x05
    magic: bytes = None
    raknet_version: int = None
    mtu_size: int = None

    def decode_payload(self):
        self.magic = self.read_magic()
        self.raknet_version = self.read_ubyte()
        self.mtu_size = len(self.read_remaining())
