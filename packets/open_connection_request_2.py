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


class OpenConnectionRequest2(Packet):
    packet_id = 0x07
    magic: bytes = None
    server_address: tuple = None  # ('255.255.255.255', 19132, 4)
    mtu_size: int = None
    client_guid: int = None

    def decode_payload(self):
        self.magic = self.read_magic()
        self.server_address = self.read_address()
        self.mtu_size = self.read_short()
        self.client_guid = self.read_long()
