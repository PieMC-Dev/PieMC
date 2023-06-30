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

from buffer import Buffer
import config
from colorama import Fore, Style


class Packet(Buffer):
    packet_id = 0x00
    def decode_header(self):
        return self.read_byte()

    def encode_header(self):
        self.write_byte(self.packet_id)

    def decode(self):
        self.decode_header()
        if hasattr(self, 'decode_payload'):
            self.decode_payload()

    def encode(self):
        self.encode_header()
        if hasattr(self, 'encode_payload'):
            self.encode_payload()
