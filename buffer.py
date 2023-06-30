#
#
# //--------\\    [----------]   ||--------]   ||\      /||    ||----------]
# ||        ||         ||        ||            ||\\    //||    ||
# ||        //         ||        ||======|     || \\  // ||    ||
# ||-------//          ||        ||            ||  \\//  ||    ||
# ||                   ||        ||            ||   —–   ||    ||
# ||              [----------]   ||--------]   ||        ||    ||----------]
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# @author PieMC Team
# @link http://www.PieMC-Dev.github.io/
#
#
#

import struct


class UnsupportedIPVersion(Exception):
    pass


class EOSError(Exception):
    pass


class BuffError(Exception):
    pass


class Buffer:

    def __init__(self, data: bytes = b'', pos=0):
        if not isinstance(data, bytes):
            data = bytes(str(data), 'utf-8')
        self.data = data
        self.pos = pos

    def write(self, data):  # Write data to buffer
        if not isinstance(data, bytes):
            data = bytes(str(data), 'utf-8')
        self.data += bytearray(data)

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
            data = str(data).encode()
        self.write(struct.pack('b', int(data)))

    def read_ubyte(self):
        return struct.unpack('B', self.read(1))[0]

    def write_ubyte(self, data):
        if not isinstance(data, bytes):
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
        if len(self.data) - self.pos < 16:
            raise EOSError('End of buffer')
        return self.read(16)

    def write_magic(self, data=b'00ffff00fefefefefdfdfdfd12345678'):
        if not isinstance(data, bytes):
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

    def read_int(self):
        return struct.unpack(">i", self.read(4))[0]

    def write_int(self, data):
        self.write(struct.pack('>i', data))

    def read_uint(self):
        return struct.unpack(">I", self.read(4))[0]

    def write_uint(self, data):
        self.write(struct.pack('>I', data))

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
        if not isinstance(data, bytes):
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

    def read_var_int(self):
        value: int = 0
        for i in range(0, 35, 7):
            if self.feos():
                raise EOSError("Data position exceeded")
            number = self.read_ubyte()
            value |= ((number & 0x7f) << i)
            if (number & 0x80) == 0:
                return value
        raise BuffError("VarInt is too big")

    def write_var_int(self, value: int) -> None:
        value &= 0xffffffff
        for i in range(0, 5):
            to_write: int = value & 0x7f
            value >>= 7
            if value != 0:
                self.write_ubyte(to_write | 0x80)
            else:
                self.write_ubyte(to_write)
                break
