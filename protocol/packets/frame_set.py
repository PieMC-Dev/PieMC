from packet import Packet
from ..protocol_info import ProtocolInfo

class FrameSet(Packet):
    packet_id = ProtocolInfo.FRAME_SET
    clientbound: bool = False
    serverbound: bool = True

    def decode_payload(self):
        pass
