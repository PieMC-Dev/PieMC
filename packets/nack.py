from packets.acknowledgement import Acknowledgement
from ProtocolInfo import ProtocolInfo


class Nack(Acknowledgement):
    def __init__(self, data: bytes = b"", pos: int = 0):
        super().__init__(data, pos)
        self.packet_id: int = ProtocolInfo.NACK