from ProtocolInfo import ProtocolInfo
from packets.acknowledgement import Acknowledgement


class Ack(Acknowledgement):
    packet_id = ProtocolInfo.ACK
