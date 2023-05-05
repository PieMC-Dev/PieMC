from packet import Packet
from ..protocol_info import ProtocolInfo

class Disconnect(Packet):
    packet_id = ProtocolInfo.DISCONNECT
    clientbound: bool = True
    serverbound: bool = True
