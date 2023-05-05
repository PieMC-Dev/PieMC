from packet import Packet
from ..protocol_info import ProtocolInfo

class ConnectionRequest(Packet):
    packet_id = ProtocolInfo.CONNECTION_REQUEST
    clientbound: bool = False
    serverbound: bool = True

    def decode_payload(self):
        self.client_guid = self.read_unsigned_long_be()
        self.client_timestamp = self.read_unsigned_long_be()
