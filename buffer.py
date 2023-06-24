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
        try:
            self.data += data
        except TypeError:
            self.data += data.encode('utf-8')

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
        self.write_byte(data)

    def read_byte(self):
        return struct.unpack('b', self.read(1))[0]

    def write_byte(self, data):
        if not (data is bytes):
            data = data.encode()
        self.write(struct.pack('b', data))

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
            data = data.encode()
        self.write(data)

    def read_long(self):
        return struct.unpack('>q', self.read(8))[0]

    def write_long(self, data):
        self.write(struct.pack('>q', data))

    def read_bool(self):
        return struct.unpack('?', self.read(1))[0]

    def write_bool(self, data):
        self.write(struct.pack('?', data))

    def read_string(self):
        length = self.read_short()
        string = self.read(length).decode('utf-8')
        return string

    def write_string(self, data):
        self.write_short(len(data))
        if not (data is bytes):
            data = data.encode()
        self.write(data)

    def read_address(self):
        ipv = self.read_byte()
        if ipv == 4:
            hostname_parts = []
            for part in range(4):
                hostname_parts.append(str(~self.read_byte() & 0xff))
            hostname = ".".join(hostname_parts)
            port = self.read_unsigned_short()
            return (hostname, port, ipv)
        else:
            raise UnsupportedIPVersion('IP version is not 4')
