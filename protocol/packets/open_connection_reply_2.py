from packet import Packet
from ..protocol_info import ProtocolInfo

class OpenConnectionReply2(Packet):
    packet_id = ProtocolInfo.OPEN_CONNECTION_REPLY_2
    clientbound: bool = True
    serverbound: bool = False
    magic: bytes = ProtocolInfo.MAGIC
    server_guid: int = 0
    client_hostname: str = "0.0.0.0"
    client_port: int = 0
    mtu_size: int = 0
    use_encryption: bool = False

    def encode_payload(self):
        self.write(self.magic)
        self.write_unsigned_long_be(self.server_guid)
        self.write_address(self.client_hostname, self.client_port)
        self.write_unsigned_short_be(self.mtu_size)
        self.write_bool(self.use_encryption)
