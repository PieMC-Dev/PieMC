from packet import Packet
from ..protocol_info import ProtocolInfo

class IncompatibleProtocolVersion(Packet):
    packet_id = ProtocolInfo.INCOMPATIBLE_PROTOCOL_VERSION
    clientbound: bool = True
    serverbound: bool = False
    protocol_version: int = 0
    magic: bytes = ProtocolInfo.MAGIC
    server_guid: int = 0

    def encode_payload(self):
        self.write_unsigned_byte(self.protocol_version)
        self.write(self.magic)
        self.write_unsigned_long_be(self.server_guid)
