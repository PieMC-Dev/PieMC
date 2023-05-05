from packet import Packet
from ..protocol_info import ProtocolInfo

class OfflinePong(BinaryStream):
    packet_id = ProtocolInfo.OFFLINE_PONG
    clientbound: bool = True
    serverbound: bool = False
    client_timestamp: int = 0
    magic: bytes = ProtocolInfo.MAGIC
    server_guid: int = 0
    server_name: str = ""

    def encode_payload(self):
        self.write_unsigned_long_be(self.client_timestamp)
        self.write_unsigned_long_be(self.server_guid)
        self.write(self.magic)
        self.write_string(self.server_name)
