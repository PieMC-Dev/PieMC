from packet import Packet
from ..protocol_info import ProtocolInfo

class OpenConnectionReply1(Packet):
    packet_id = ProtocolInfo.OPEN_CONNECTION_REPLY_1
    clientbound: bool = True
    serverbound: bool = False
    magic: bytes = ProtocolInfo.MAGIC
    server_guid: int = 0
    use_security: bool = False
    mtu_size: int = 0

    def encode_payload(self):
       self.write(self.magic)
       self.write_unsigned_long_be(self.server_guid)
       self.write_bool(self.use_security)
       self.write_unsigned_short_be(self.mtu_size)
