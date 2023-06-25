import struct


class UnsupportedIPVersion(BaseException):
    pass


class EOSError(BaseException):
    pass


class Buffer:
    def __init__(self, data: bytes = b'', pos=0):
        self.data = data
        self.pos = pos

    def write(self, data):  # Write data to buffer
        if not (data is bytes):
            data = data.encode('utf-8')
        self.data += data

    def read(self, size):  # Read data from buffer
        if not self.feos():
            self.pos += size
            return self.data[self.pos - size:self.pos]
        else:
            raise EOSError('End of buffer')

    def read_remaining(self):  # Read remaining data
        return self.read(len(self.data) - self.pos)

    def feos(self):  # Is end of buffer?
        return bool(len(self.data) <= self.pos)

    def read_packet_id(self):  # Read Packet ID
        return self.read_byte()

    def write_packet_id(self, data):
        self.write_byte(str(data))

    def read_byte(self):
        return struct.unpack('b', self.read(1))[0]

    def write_byte(self, data):
        if not isinstance(data, bytes):
            data = str(data).encode('utf-8')
        self.write(struct.pack('b', data))

    def read_ubyte(self):
        return struct.unpack('B', self.read(1))[0]

    def write_ubyte(self, data):
        if not (data is bytes):
            data = data.encode('utf-8')
        self.write(struct.pack('B', data))

    def read_short(self):
        return struct.unpack('>h', self.read(2))[0]

    def write_short(self, data):
        self.write(struct.pack('>h', data))

    def read_unsigned_short(self):
        return struct.unpack('>H', self.read(2))[0]

    def write_unsigned_short(self, data):
        self.write(struct.pack('>H', data))

    def read_magic(self):
        return self.read(16)

    def write_magic(self, data=b'00ffff00fefefefefdfdfdfd12345678'):
        if not (data is bytes):
            data = data.encode('utf-8')
        self.write(data)

    def read_long(self):
        return struct.unpack('>q', self.read(8))[0]

    def write_long(self, data):
        self.write(struct.pack('>q', data))

    def read_ulong(self):
        return struct.unpack('>Q', self.read(8))[0]

    def write_ulong(self, data):
        self.write(struct.pack('>Q', data))

    def read_bool(self):
        return struct.unpack('?', self.read(1))[0]

    def write_bool(self, data):
        self.write(struct.pack('?', data))

    def read_uint24le(self):
        return struct.unpack("<I", self.read(3) + b'\x00')[0]

    def write_uint24le(self, data):
        self.write(struct.pack("<I", data)[:3])

    def read_string(self):
        length = self.read_short()
        string = self.read(length).decode('utf-8')
        return string

    def write_string(self, data):
        self.write_short(len(data))
        if not (data is bytes):
            data = data.encode('utf-8')
        self.write(data)

    def read_address(self):
        ipv = self.read_byte()
        if ipv == 4:
            hostname_parts = []
            for part in range(4):
                hostname_parts.append(str(~self.read_byte() & 0xff))
            hostname = ".".join(hostname_parts)
            port = self.read_unsigned_short()
            return hostname, port, ipv
        else:
            raise UnsupportedIPVersion('IP version is not 4')

    def write_address(self, address: tuple):
        if address[2] == 4:
            self.write_byte(address[2])
            hostname_parts: list = address[0].split('.')
            for part in hostname_parts:
                self.write_byte(~int(part) & 0xff)
            self.write_short(address[1])
        else:
            raise UnsupportedIPVersion('IP version is not 4')
