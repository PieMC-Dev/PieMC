from packet import Packet
from ..protocol_info import ProtocolInfo

class Frame(Packet):
    packet_id = ProtocolInfo.FRAME
    clientbound: bool = True
    serverbound: bool = True
    reliability: int = 0
    fragmented: bool = False
    reliable_frame_index: int = 0
    sequenced_frame_index: int = 0
    ordered_frame_index: int = 0
    order_channel: int = 0
    compound_size: int = 0
    compound_id: int = 0
    index: int = 0
    body: bytes = b""

    def decode(self):
        flags: int = self.read_unsigned_byte()
        self.reliability = (flags & 0xf4) >> 5
        self.fragmented = (flags & 0x10) > 0
        body_length: int = self.read_unsigned_short_be() >> 3
        if 2 <= self.reliability <= 7 and self.reliability != 5:
            self.reliable_frame_index = self.read_unsigned_triad_le()
        if self.reliability == 1 or self.reliability == 4:
            self.sequenced_frame_index = self.read_unsigned_triad_le()
        if 1 <= self.reliability <= 4 and self.reliability != 2 or self.reliability == 7:
            self.ordered_frame_index = self.read_unsigned_triad_le()
        if self.fragmented:
            self.compound_size = self.read_unsigned_int_be()
            self.compound_id = self.read_unsigned_short_be()
            self.index = self.read_unsigned_int_be()
        self.body = self.read(body_length)

    def encode(self):
        self.write_unsigned_byte((self.reliability << 5) | (0x10 if self.fragmented else 0))
        self.write_unsigned_short_be(len(self.body) << 3)
        if 2 <= self.reliability <= 7 and self.reliability != 5:
            self.write_unsigned_triad_le(self.reliable_frame_index)
        if self.reliability == 1 or self.reliability == 4:
            self.write_unsigned_triad_le(self.sequenced_frame_index)
        if 1 <= self.reliability <= 4 and self.reliability != 2 or self.reliability == 7:
            self.write_unsigned_triad_le(self.ordered_frame_index)
        if self.fragmented:
            self.write_unsigned_int_be(self.compound_size)
            self.write_unsigned_short_be(self.compound_id)
            self.write_unsigned_int_be(self.index)
        self.write(self.body)

    def get_size(self):
        length: int = 3
        if 2 <= self.reliability <= 7 and self.reliability
!= 5:
            length += 3
        if self.reliability == 1 or self.reliability == 4:
            length += 3
        if 1 <= self.reliability <= 4 and self.reliability
!= 2 or self.reliability == 7:
            length += 4
        if self.fragmented:
            length += 10
        length += len(self.body)
        return length
