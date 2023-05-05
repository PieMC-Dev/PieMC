from packet import packet
from ..protocol_info import ProtocolInfo

class OnlinePing(Packet):
    packet_id = ProtocolInfo.ONLINE_PING
    clientbound: bool = False
    serverbound: bool = True
    client_timestamp: int = 0

    def decode_payload(self):
        self.client_timestamp = self.read_unsigned_long_be()
