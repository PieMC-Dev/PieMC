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


class IncompatibleProtocolVersion(Packet):
    packet_id = 0x19
    raknet_version: int = None
    magic: bytes = None
    server_guid: int = None

    def encode_payload(self):
        self.write_byte(self.raknet_version)
        self.write_magic(self.magic)
        self.write_long(self.server_guid)
