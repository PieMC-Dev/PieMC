from packet import Packet
from ..binary_stream import BinaryStream

class Acknowledgement(Packet):
    sequence_numbers: list = []

    def decode_payload(self):
        self.sequence_numbers.clear()
        count: int = self.read_unsigned_short_be()
        for i in range(0, count):
            single: bool = self.read_bool()
            if not single:
                index: int = self.read_unsigned_triad_le()
                end_index: int = self.read_unsigned_triad_le()
                while index <= end_index:
                    self.sequence_numbers.append(index)
                    index += 1
            else:
                self.sequence_numbers.append(self.read_unsigned_triad_le())

    def encode_payload(self):
        self.sequence_numbers.sort()
        temp_buffer = BinaryStream()
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
                        temp_buffer.write_unsigned_triad_le(start_index)
                        temp_buffer.write_unsigned_triad_le(end_index)
                        start_index = end_index = current_index
                    else:
                        temp_buffer.write_bool(False)
                        temp_buffer.write_unsigned_triad_le(start_index)
                        temp_buffer.write_unsigned_triad_le(end_index)
                        start_index = end_index = current_index
                    count += 1
            if start_index == end_index:
                temp_buffer.write_bool(True)
                temp_buffer.write_unsigned_triad_le(start_index)
            else:
                temp_buffer.write_bool(False)
                temp_buffer.write_unsigned_triad_le(start_index)
                temp_buffer.write_unsigned_triad_le(end_index)
            count += 1
            self.write_unsigned_short_be(count)
            self.write(temp_buffer.data)
