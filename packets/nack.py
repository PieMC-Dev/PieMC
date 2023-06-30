from packets.acknowledgement import Acknowledgement
from ProtocolInfo import ProtocolInfo


class Nack(Acknowledgement):
    packet_id = ProtocolInfo.NACK
