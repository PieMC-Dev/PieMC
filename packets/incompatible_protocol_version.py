from packets.packet import Packet
from ProtocolInfo import ProtocolInfo

class IncompatibleProtocolVersion(Packet):
    packet_id = ProtocolInfo.INCOMPATIBLE_PROTOCOL_VERSION
    protocol_version: int = 0
    magic: bytes = b""
    server_guid: int = 0

    def decode_payload(self) -> None:
        self.protocol_version = self.read_unsigned_byte()
        self.magic = self.read(16)
        self.server_guid = self.read_unsigned_long_be()
    
    def encode_payload(self) -> None:
        self.write_unsigned_byte(self.protocol_version)
        self.write(self.magic)
        self.write_unsigned_long_be(self.server_guid)