from packet import Packet
from ..protocol_info import ProtocolInfo

class OpenConnectionRequest2(Packet):
    packet_id = ProtocolInfo.OPEN_CONNECTION_REQUEST_2
    clientbound: bool = False
    serverbound: bool = True

    def decode_payload(self):
        self.magic = self.read(16)
        self.address = self.read_address()
        self.mtu_size = self.read_unsigned_short_be()
        self.client_guid = self.read_unsigned_long_be()
