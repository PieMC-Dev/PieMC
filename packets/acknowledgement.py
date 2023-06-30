from packets.packet import Packet
from buffer import Buffer


class Acknowledgement(Packet):
    def __init__(self, data: bytes = b"", pos: int = 0):
        super().__init__(data, pos)
        self.sequence_numbers: list[int] = []

    def decode_payload(self) -> None:
        self.sequence_numbers.clear()
        count: int = self.read_short()
        for i in range(0, count):
            single: bool = self.read_bool()
            if not single:
                index: int = self.read_uint24le()
                end_index: int = self.read_uint24le()
                while index <= end_index:
                    self.sequence_numbers.append(index)
                    index += 1
            else:
                self.sequence_numbers.append(self.read_uint24le())

    def encode_payload(self) -> None:
        self.sequence_numbers.sort()
        temp_buffer: Buffer = Buffer()
        count: int = 0
        if len(self.sequence_numbers) > 0:
            start_index: int = self.sequence_numbers[0]
            end_index: int = self.sequence_numbers[0]
            for pointer in range(1, len(self.sequence_numbers)):
                current_index: int = self.sequence_numbers[pointer]
                diff: int = current_index - end_index
                if diff == 1:
                    end_index: int = current_index
                elif diff > 1:
                    if start_index == end_index:
                        temp_buffer.write_bool(True)
                        temp_buffer.write_uint24le(start_index)
                        start_index = end_index = current_index
                    else:
                        temp_buffer.write_bool(False)
                        temp_buffer.write_uint24le(start_index)
                        temp_buffer.write_uint24le(end_index)
                        start_index = end_index = current_index
                    count += 1
            if start_index == end_index:
                temp_buffer.write_bool(True)
                temp_buffer.write_uint24le(start_index)
            else:
                temp_buffer.write_bool(False)
                temp_buffer.write_uint24le(start_index)
                temp_buffer.write_uint24le(end_index)
            count += 1
            self.write_short(count)
            self.write(temp_buffer.data)
