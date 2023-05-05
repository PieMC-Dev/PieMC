from packet import Packet
from ..protocol_info import ProtocolInfo

class NewIncomingConnection(Packet):
    packet_id = ProtocolInfo.NEW_INCOMING_CONNECTION
    clientbound: bool = False
    serverbound: bool = True

    def decode_payload(self):
        self.server_address = self.read_address()
        self.internal_address = self.read_address()
