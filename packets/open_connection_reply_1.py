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


class OpenConnectionReply1(Packet):
    packet_id = 0x06
    magic: bytes = None
    server_guid: int = None
    use_security: bool = None
    mtu_size: int = None
    
    def encode_payload(self):
        self.write_magic(self.magic)
        self.write_long(self.server_guid)
        self.write_bool(self.use_security)
        self.write_short(self.mtu_size)
