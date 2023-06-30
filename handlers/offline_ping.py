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
from packets.offline_ping import OfflinePing
from packets.offline_pong import OfflinePong


class OfflinePingHandler:
    @staticmethod
    def handle(packet: OfflinePing, server, connection: tuple):
        packet.decode()
        if config.DEBUG:
            debug_info = [
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Client Timestamp: {str(packet.client_timestamp)}",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - MAGIC: {str(packet.magic)}",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Client GUID: {str(packet.client_guid)}"
            ]
            print("\n".join(debug_info))

        pong = OfflinePong()
        pong.client_timestamp = packet.client_timestamp
        pong.server_guid = server.guid
        pong.magic = packet.magic
        server.update_server_status()
        pong.server_name = server.server_name
        pong.encode()
        server.send(pong.data, connection)

        if config.DEBUG:
            debug_info = [
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} Sent Packet:",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet ID: {str(pong.packet_id)}",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet Body: {str(pong.data[1:])}",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet Type: Offline Pong",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Client Timestamp: {str(pong.client_timestamp)}",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Server GUID: {str(pong.server_guid)}",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - MAGIC: {str(pong.magic)}",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Server Name: {str(pong.server_name)}"
            ]
            print("\n".join(debug_info))

