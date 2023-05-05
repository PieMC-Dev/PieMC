from packet import Packet
from ..protocol_info import ProtocolInfo

class OnlinePong(Packet):
    packet_id = ProtocolInfo.ONLINE_PONG
    clientbound: bool = True
    serverbound: bool = False
    client_timestamp: int = 0
    server_timestamp:int = 0

    def decode_payload(self):
        self.client_timestamp = self.read_unsigned_long_be()
        self.server_timestamp = self.read_unsigned_long_be()
