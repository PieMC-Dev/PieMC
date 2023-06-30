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

from packets.packet import Packet
from buffer import Buffer
import zlib


class GamePacket(Packet):
    packet_id = 0xfe

    def __init__(self, data: bytes = b'', pos=0):
        super().__init__(data, pos)
        self.body = None

    def decode_payload(self):
        self.body = zlib.decompress(self.read_remaining(), -zlib.MAX_WBITS, 1024 * 1024 * 8)

    def encode_payload(self):
        compress = zlib.compressobj(1, zlib.DEFLATED, -zlib.MAX_WBITS)
        compressed_data = compress.compress(self.body)
        compressed_data += compress.flush()
        self.write(compressed_data)

    def read_packets_data(self):
        buffer = Buffer(self.body)
        packets_data = []
        while not buffer.feos():
            packets_data.append(buffer.read(buffer.read_var_int()))
        return packets_data

    def write_packet_data(self, data):
        buffer = Buffer()
        buffer.write_var_int(len(data))
        buffer.write(data)
        if hasattr(self, "body"):
            self.body += buffer.data
        else:
            self.body = buffer.data
