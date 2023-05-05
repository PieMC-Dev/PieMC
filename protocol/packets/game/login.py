from ..packet import Packet
from ...protocol_info import GameProtocolInfo

class Login(Packet):
    packet_id = GameProtocolInfo.LOGIN
    clientbound: bool = False
    serverbound: bool = True

    def decode_payload(self):
        self.protocol_version = self.read_unsigned_int_be()
        self.payload = self.read_remaining()
