from packets.packet import Packet
from handlers.InternetAddress import InternetAddress

class OpenConnectionRequest2(Packet):
    packet_id = 0x07
    magic: bytes = b""
    server_address: InternetAddress = InternetAddress("255.255.255.255", 0)
    mtu_size: int = 0
    client_guid: int = 0

    def decode_payload(self) -> None:
        self.magic = self.read(16)
        self.server_address = self.read_address()
        self.mtu_size = self.read_unsigned_short_be()
        self.client_guid = self.read_unsigned_long_be()
        
    def encode_payload(self) -> None:
        self.write(self.magic)
        self.write_address(self.server_address)
        self.write_unsigned_short_be(self.mtu_size)
        self.write_unsigned_long_be(self.client_guid)
