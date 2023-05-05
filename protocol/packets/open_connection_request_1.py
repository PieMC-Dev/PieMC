from packet import Packet
from ..protocol_info import ProtocolInfo

class OpenConnectionRequest1(Packet):
    packet_id = ProtocolInfo.OPEN_CONNECTION_REQUEST_1
    clientbound: bool = False
    serverbound: bool = True

    def decode_payload(self):
       self.magic = self.read(16)
       self.protocol_version = self.read_unsigned_byte()
       self.mtu_size = self.read_remaining()
