from packets.packet import Packet

class OpenConnectionRequest1(Packet):
    packet_id = 0x05
    magic: bytes = b""
    raknet_version: int = 0
    mtu_size: int = 0
  
    def decode_payload(self):
        self.magic = self.read_magic()
        self.raknet_version = int(self.read_byte())
        self.mtu_size = len(self.read_remaining())