from packets.packet import Packet

class OpenConnectionRequest1(Packet):
    packet_id = 0x05
    magic: bytes = b""
    protocol_version: int = 0
    mtu_size: int = 0
  
    def decode_payload(self) -> None:
        #print("MAGIC!!!!!!!!!!!!!!!!!!")
        #print(self.magic)
        #self.magic = self.read(16)
        self.protocol_version = self.read_unsigned_byte()
        self.mtu_size = len(self.read_remaining())
        
    def encode_payload(self) -> None:
        self.write(self.magic)
        self.write_unsigned_byte(self.protocol_version)
        self.write(b"\x00" * self.mtu_size)

    def read_unsigned_byte(self) -> int:
        return self.read_unsigned_byte(self.read(1))