from ..packet import Packet
from ...protocol_info import GameProtocolInfo

class PlayStatus(Packet):
    packet_id = GameProtocolInfo.PLAY_STATUS
    clientbound: bool = True
    serverbound: bool = False
    status: int = 2

    def encode_payload(self):
        self.write_unsigned_int_be(status)
