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


class OpenConnectionRequest1(Packet):
    packet_id = 0x05
    magic: bytes = None
    raknet_version: int = None
    mtu_size: int = None

    def decode_payload(self):
        self.magic = self.read_magic()
        self.raknet_version = int(self.read_byte())
        self.mtu_size = len(self.read_remaining())
