from acknowledgement import Acknowlegdement
from ..protocol_info import ProtocolInfo

class NACK(Acknowledgement):
    packet_id = ProtocolInfo.NACK
    clientbound: bool = True
    serverbound: bool = True
