import struct

class BinaryStream:

    def __init__(self, data: bytes = b"", pos: int = 0):
        self.data = data
        self.pos = pos

    def read(self, size: int):
        self.pos += size
        return self.data[self.pos - size:self.pos]

    def write(self, data: bytes):
        self.data += data

    def read_remaining(self):
        return self.read(len(self.data) - self.pos)

    def feos(self):
        return (len(self.data) <= self.pos)

    def read_byte(self):
        return struct.unpack("b", self.read(1))[0]

    def write_byte(self, value: int):
        self.write(struct.pack("b", value))

    def read_unsigned_byte(self):
        return struct.unpack("B", self.read(1))[0]

    def write_unsigned_byte(self, value: int):
        self.write(struct.pack("B", value))

    def read_bool(self):
        return struct.unpack("?", self.read(1))[0]

    def write_bool(self, value: bool):
        self.write(struct.pack("?", value))

    def read_short_be(self):
        return struct.unpack(">h", self.read(2))[0]

    def write_short_be(self, value: int):
        self.write(struct.pack(">h", value))

    def read_unsigned_short_be(self):
        return struct.unpack(">H", self.read(2))[0]

    def write_unsigned_short_be(self, value: int):
        self.write(struct.pack(">H", value))

    def read_short_le(self):
        return struct.unpack("<h", self.read(2))[0]

    def write_short_le(self, value: int):
        self.write(struct.pack("<h", value))

    def read_unsigned_short_le(self):
        return struct.unpack("<H", self.read(2))[0]

    def write_unsigned_short_le(self, value: int):
        self.write(struct.pack("<H", value))

    def read_triad_be(self):
        return struct.unpack(">i", b"\x00" + self.read(3))[0]

    def write_triad_be(self, value: int):
        self.write(struct.pack(">i", value)[1:4])

    def read_unsigned_triad_be(self):
        return struct.unpack(">I", b"\x00" + self.read(3))[0]

    def write_unsigned_triad_be(self, value: int):
        self.write(struct.pack(">I", value)[1:4])

    def read_triad_le(self):
        return struct.unpack("<i", self.read(3) + b"\x00")[0]

    def write_triad_le(self, value: int):
        self.write(struct.pack("<i", value)[:3])

    def read_unsigned_triad_le(self):
        return struct.unpack("<I", self.read(3) + b"\x00")[0]

    def write_unsigned_triad_le(self, value: int):
        self.write(struct.pack("<I", value)[:3])

    def read_int_be(self):
        return struct.unpack(">i", self.read(4))[0]

    def write_int_be(self, value: int):
        self.write(struct.pack(">i", value))

    def read_unsigned_int_be(self):
        return struct.unpack(">I", self.read(4))[0]

    def write_unsigned_int_be(self, value: int):
        self.write(struct.pack(">I", value))

    def read_int_le(self):
        return struct.unpack("<i", self.read(4))[0]

    def write_int_le(self, value: int):
        self.write(struct.pack("<i", value))

    def read_unsigned_int_le(self):
        return struct.unpack("<I", self.read(4))[0]

    def write_unsigned_int_le(self, value: int):
        self.write(struct.pack("<I", value))

    def read_long_be(self):
        return struct.unpack(">q", self.read(8))[0]

    def write_long_be(self, value: int):
        self.write(struct.pack(">q", value))

    def read_unsigned_long_be(self):
        return struct.unpack(">Q", self.read(8))[0]

    def write_unsigned_long_be(self, value: int):
        self.write(struct.pack(">Q", value))

    def read_long_le(self):
        return struct.unpack("<q", self.read(8))[0]

    def write_long_le(self, value: int):
        self.write(struct.pack("<q", value))

    def read_unsigned_long_le(self):
        return struct.unpack("<Q", self.read(8))[0]

    def write_unsigned_long_le(self, value: int):
        self.write(struct.pack("<Q", value))

    def read_float_be(self):
        return struct.unpack(">f", self.read(4))[0]

    def write_float_be(self, value: int):
        self.write(struct.pack(">f", value))

    def read_float_le(self):
        return struct.unpack("<f", self.read(4))[0]

    def write_float_le(self, value: int):
        self.write(struct.pack("<f", value))

    def read_double_be(self):
        return struct.unpack(">d", self.read(8))[0]

    def write_double_be(self, value: int):
        self.write(struct.pack(">d", value))

    def read_double_le(self):
        return struct.unpack("<d", self.read(8))[0]

    def write_double_le(self, value: int):
        self.write(struct.pack("<d", value))

    def read_var_int(self):
        value: int = 0
        for i in range(0, 35, 7):
            if self.feos():
                raise Exception("Data position exceeded")
            else:
                number: int = self.read_unsigned_byte()
                value |= ((number & 0x7f) << i)
                if (number & 0x80) == 0:
                    return value
        raise Exception("VarInt is too big")

    def write_var_int(self, value: int):
        data: bytes = b""
        value &= 0xffffffff
        for i in range(0, 5):
            to_write: int = value & 0x7f
            value >>= 7
            if value != 0:
                self.write_unsigned_byte(to_write | 0x80)
            else:
                self.write_unsigned_byte(to_write)
                break

    def read_signed_var_int(self):
        raw: int = self.read_var_int()
        temp: int = -(raw >> 1) - 1 if (raw & 1) else raw >> 1
        return temp

    def write_signed_var_int(self, value: int):
        self.write_var_int(value << 1 if value >= 0 else (-value - 1) << 1 | 1)

    def read_var_long(self):
        value: int = 0
        for i in range(0, 70, 7):
            if self.feos():
                raise Exception("Data position exceeded")
            number: int = self.read_unsigned_byte()
            value |= ((number & 0x7f) << i)
            if (number & 0x80) == 0:
                return value
            raise Exception("VarLong is too big")

    def write_var_long(self, value: int):
        for i in range(0, 10):
            to_write: int = value & 0x7f
            value >>= 7
            if value != 0:
                self.write_unsigned_byte(to_write | 0x80)
            else:
                self.write_unsigned_byte(to_write)
                break

    def read_signed_var_long(self):
        raw: int = self.read_var_long()
        temp: int = -(raw >> 1) - 1 if (raw & 1) else raw >> 1
        return temp

    def write_signed_var_long(self, value: int):
        self.write_var_long(value << 1 if value >= 0 else (-value - 1) << 1 | 1)
