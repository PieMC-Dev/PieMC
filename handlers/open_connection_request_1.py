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
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - MAGIC: {str(packet.magic)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - RakNet Version: {str(packet.raknet_version)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - MTU: {str(packet.mtu_size)}")
        if packet.raknet_version == server.protocol_version:
            new_packet: OpenConnectionReply1 = OpenConnectionReply1()
            new_packet.magic = packet.magic
            new_packet.server_guid = server.guid
            new_packet.use_security = False
            new_packet.mtu_size = packet.mtu_size
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} Sent Packet:")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet ID: {str(new_packet.packet_id)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet Body: {str(new_packet.data[1:])}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet Type: Open Connection Reply 1")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - MAGIC: {str(new_packet.magic)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Server GUID: {str(new_packet.server_guid)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Use Security: {str(new_packet.use_security)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - MTU Size: {str(new_packet.mtu_size)}")
        else:
            new_packet: IncompatibleProtocolVersion = IncompatibleProtocolVersion()
            new_packet.raknet_version = server.protocol_version
            new_packet.magic = packet.magic
            new_packet.server_guid = server.guid
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} Sent Packet:")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet ID: {str(new_packet.packet_id)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet Body: {str(new_packet.data[1:])}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet Type: Incompatible RakNet Version")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Server RakNet Version: {str(new_packet.raknet_version)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - MAGIC: {str(new_packet.magic)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Server GUID: {str(new_packet.server_guid)}")
        new_packet.encode()
        return new_packet.data
