import struct


class Buffer:
    def __init__(self, data: bytes = b'', pos=0):
        self.data = data
        self.pos = pos

    def write(self, data):  # Write data to buffer
        self.data += data

    def read(self, size):  # Read data from buffer
        self.pos += size
        return self.data[self.pos - size:self.pos]

    def read_remaining(self):  # Read remaining data
        return self.read(len(self.data) - self.pos)

    def feos(self):  # Is end of buffer?
        return bool(len(self.data) <= self.pos)

    def read_packet_id(self):  # Read Packet ID
        return self.read_byte()

    def write_packet_id(self, data):
        self.write_byte(data)

    def read_byte(self):
        return struct.unpack('b', self.read(1))[0]

    def write_byte(self, data):
        self.write(struct.pack('b', data)[0])

    def read_short(self):
        return struct.unpack('>h', self.read(2))[0]

    def write_short(self, data):
        self.write(struct.pack('>h', data)[0])

    def read_unsigned_short(self):
        return struct.unpack('>H', self.read(2))[0]

    def write_unsigned_short(self, data):
        self.write(struct.pack('>H', data)[0])

    def read_magic(self):
        return self.read(16)

    def write_magic(self, data='00ffff00fefefefefdfdfdfd12345678'):
        self.write(data)

    def read_long(self):
        return struct.unpack('>q', self.read(8))[0]

    def write_long(self, data):
        self.write(struct.pack('>q', data)[0])

    def read_bool(self):
        return struct.unpack('?', self.read(1))[0]

    def write_bool(self, data):
        self.write(struct.pack('?', data)[0])

    def read_string(self):
        length = self.read_short()
        string = str(self.read(length))
        return string

    def write_string(self, data):
        self.write_short(len(data))
        self.write(data)
