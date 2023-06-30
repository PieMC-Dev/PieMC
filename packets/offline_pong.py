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


class OfflinePong(Packet):
    packet_id = 0x1c
    client_timestamp: int = None
    server_guid: int = None
    magic: bytes = None
    server_name: bytes = None

    def encode_payload(self):
        self.write_long(self.client_timestamp)
        self.write_long(self.server_guid)
        if not isinstance(self.magic, bytes):
            self.magic = self.magic.encode('utf-8')
        self.write_magic(self.magic)
        self.write_string(self.server_name)
