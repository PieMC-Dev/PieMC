from packet import Packet
from ..protocol_info import ProtocolInfo
from frame import Frame

class FrameSet(Packet):
    packet_id = ProtocolInfo.FRAME_SET
    clientbound: bool = True
    serverbound: bool = True
    sequence_number: int = 0
    frames: list = []

    def decode_payload(self):
        self.sequence_number = self.read_unsigned_triad_le()
        while not self.feos():
            frame = Frame(self.data[self.pos:])
            frame.decode()
            self.frames.append(frame)
            self.pos += frame.get_size()

    def get_size(self):
        length = 4
        for frame in self.frames:
            length += frame.get_size()
        return length
