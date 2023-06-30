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

import config
from colorama import Fore
from packets.open_connection_request_1 import OpenConnectionRequest1
from packets.open_connection_reply_1 import OpenConnectionReply1
from packets.incompatible_protocol_version import IncompatibleProtocolVersion


class OpenConnectionRequest1Handler:
    @staticmethod
    def handle(packet: OpenConnectionRequest1, server, connection: tuple):
        packet.decode()
        if config.DEBUG:
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - MAGIC: {packet.magic}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - RakNet Version: {packet.raknet_version}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - MTU: {packet.mtu_size}")

        if packet.raknet_version == server.raknet_version:
            new_packet = OpenConnectionReply1()
            new_packet.magic = packet.magic
            new_packet.server_guid = server.guid
            new_packet.use_security = False
            new_packet.mtu_size = packet.mtu_size

            if config.DEBUG:
                debug_info = [
                    f"{Fore.BLUE}[DEBUG]{Fore.WHITE} Sent Packet:",
                    f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet ID: {new_packet.packet_id}",
                    f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet Body: {new_packet.data[1:]}",
                    f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet Type: Open Connection Reply 1",
                    f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - MAGIC: {new_packet.magic}",
                    f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Server GUID: {new_packet.server_guid}",
                    f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Use Security: {new_packet.use_security}",
                    f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - MTU Size: {new_packet.mtu_size}"
                ]
                print("\n".join(debug_info))
        else:
            new_packet = IncompatibleProtocolVersion()
            new_packet.raknet_version = server.protocol_version
            new_packet.magic = packet.magic
            new_packet.server_guid = server.guid

            if config.DEBUG:
                debug_info = [
                    f"{Fore.BLUE}[DEBUG]{Fore.WHITE} Sent Packet:",
                    f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet ID: {new_packet.packet_id}",
                    f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet Body: {new_packet.data[1:]}",
                    f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet Type: Incompatible RakNet Version",
                    f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Server RakNet Version: {new_packet.raknet_version}",
                    f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - MAGIC: {new_packet.magic}",
                    f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Server GUID: {new_packet.server_guid}"
                ]
                print("\n".join(debug_info))

        new_packet.encode()
        return new_packet.data

