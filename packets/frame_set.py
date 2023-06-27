from packets.packet import Packet
from buffer import Buffer


class Frame(Buffer):
    reliability: int = None
    fragmented: bool = None
    reliable_frame_index: int = None
    sequenced_frame_index: int = None
    ordered_frame_index: int = None
    order_channel: int = None
    compound_size: int = None
    compound_id: int = None
    index: int = None
    body: bytes = None

    def decode(self):
        flags: int = self.read_byte()
        self.reliability = (flags & 0xf4) >> 5
        self.fragmented = (flags & 0x10) > 0
        body_length: int = self.read_unsigned_short() >> 3
        if 2 <= self.reliability <= 7 and self.reliability != 5:
            self.reliable_frame_index = self.read_uint24le()
        if self.reliability == 1 or self.reliability == 4:
            self.sequenced_frame_index = self.read_uint24le()
        if self.reliability == 3 or self.reliability == 7:
            self.ordered_frame_index = self.read_uint24le()
            self.order_channel = self.read_byte()
        if self.fragmented:
            self.compound_size = self.read_int()
            self.compound_id = self.read_short()
            self.index = self.read_int()
        self.body = self.read(body_length)

    def encode(self):
        self.write_byte((self.reliability << 5) | (0x10 if self.fragmented else 0))
        self.write_unsigned_short(len(self.body) << 3)
        if 2 <= self.reliability <= 7 and self.reliability != 5:
            self.write_uint24le(self.reliable_frame_index)
        if self.reliability == 1 or self.reliability == 4:
            self.write_uint24le(self.sequenced_frame_index)
        if self.reliability == 3 or self.reliability == 7:
            self.write_uint24le(self.ordered_frame_index)
            self.write_byte(self.order_channel)
        if self.fragmented:
            self.write_int(self.compound_size)
            self.write_short(self.compound_id)
            self.write_int(self.index)
        self.write_uint24le(self.body)

    def get_size(self):
        length: int = 3
        if 2 <= self.reliability <= 7 and self.reliability != 5:
            length += 3
        if self.reliability == 1 or self.reliability == 4:
            length += 3
        if self.reliability == 3 or self.reliability == 7:
            length += 4
        if self.fragmented:
            length += 10
        return length


class FrameSet(Packet):
    packet_id = 0x80
    sequence_number: int = None
    frames: list[Frame] = []

    def decode_payload(self):
        self.sequence_number = self.read_uint24le()
        while not self.feos():
            frame: Frame = Frame(self.data[self.pos:])
            frame.decode()
            self.frames.append(frame)
            self.pos += frame.get_size()

    def encode_payload(self):
        self.write_uint24le(self.sequence_number)
        for frame in self.frames:
            frame.encode()
            self.write(frame.data)

    def get_size(self):
        length: int = 4
        for frame in self.frames:
            length += frame.get_size()
        return length
