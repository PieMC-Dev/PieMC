from acknowledgement import Acknowlegdement
from ..protocol_info import ProtocolInfo

class ACK(Acknowledgement):
    packet_id = ProtocolInfo.ACK
    clientbound: bool = True
    serverbound: bool = True
