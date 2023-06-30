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

import socket
import config
import random
import os
from colorama import Fore, Style
import time
from packets.offline_ping import OfflinePing
from handlers.offline_ping import OfflinePingHandler
from packets.open_connection_request_1 import OpenConnectionRequest1
from handlers.open_connection_request_1 import OpenConnectionRequest1Handler
from packets.open_connection_request_2 import OpenConnectionRequest2
from handlers.open_connection_request_2 import OpenConnectionRequest2Handler
from ProtocolInfo import ProtocolInfo
from packets.acknowledgement import Ack
from packets.acknowledgement import Nack
from packets.frame_set import FrameSet

lang_dirname = "lang"
file_to_find = config.LANG + ".py"

lang_fullpath = os.path.join(os.getcwd(), lang_dirname)

if os.path.exists(lang_fullpath):
    lang_path = os.path.join(lang_fullpath, file_to_find)
    if os.path.isfile(lang_path):
        language = config.LANG
    else:
        language = 'en'
        print(f"The {config.LANG} lang doesn't exist in the {lang_dirname} directory. Using English...")
        time.sleep(5)

text = __import__('lang.' + language, fromlist=[config.LANG])

if not os.path.exists("pieuid.dat"):
    pieuid = random.randint(10 ** 19, (10 ** 20) - 1)
    with open("pieuid.dat", "w") as uid_file:
        uid_file.write(str(pieuid))
    print(str(text.CREATED_PIEUID) + ":", pieuid)


class PieMC_Server:
    def __init__(self, ip, port):
        self.server_name = None
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ip = ip
        self.port = port
        self.edition = "MCPE"
        self.protocol_version = 589
        self.version_name = "1.20.0"
        self.motd1 = config.MOTD1
        self.motd2 = config.MOTD2
        self.players_online = 2  # 2 players online XD. Update (By andiri): YES :sunglasses:
        self.max_players = config.MAX_PLAYERS
        self.gamemode_map = {
            "survival": ("Survival", 1),
            "creative": ("Creative", 2),
            "adventure": ("Adventure", 3)
        }
        self.gamemode = self.gamemode_map.get(config.GAMEMODE.lower(), ("Survival", 0))
        print(f"Gamemode {config.GAMEMODE} not exists, using Survival") if self.gamemode[1] == 0 else None
        self.port = config.PORT
        self.port_v6 = 19133
        self.guid = random.randint(1, 99999999)
        with open('pieuid.dat', 'r') as f:
            pieuid = f.read().strip()
        self.uid = pieuid
        # self.magic = '00ffff00fefefefefdfdfdfd12345678'
        self.start_time = int(time.time() * 1000)
        self.update_server_status()
        self.raknet_version = 11

    def get_time_ms(self):
        return int(time.time() * 1000) - self.start_time

    def update_server_status(self):
        self.server_name = ';'.join([
            self.edition,
            self.motd1,
            str(self.protocol_version),
            self.version_name,
            str(self.players_online),
            str(self.max_players),
            str(self.uid),
            self.motd2,
            self.gamemode[0],
            str(self.gamemode[1]),
            str(self.port),
            str(self.port_v6)
        ]) + ';'

    def send(self, data: bytes, connection: tuple):
        self.socket.sendto(data, connection)

    def start(self):
        with self.socket as server_socket:
            server_socket.bind((self.ip, self.port))
            self.socket = server_socket
            print(Fore.GREEN + Style.BRIGHT + text.RUNNING + Style.RESET_ALL)
            print(f"{text.IP}: {Fore.YELLOW}{config.HOST}{Style.RESET_ALL}")
            print(f"{text.PORT}: {Fore.YELLOW}{config.PORT}{Style.RESET_ALL}")
            print(f"{text.GAMEMODE}: {Fore.YELLOW}{config.GAMEMODE}{Style.RESET_ALL}")
            print(f"{text.MAX_PLAYERS}: {Fore.YELLOW}{config.MAX_PLAYERS}{Style.RESET_ALL}")

            try:
                while True:
                    data, client_address = server_socket.recvfrom(4096)
                    if config.DEBUG:
                        print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} New packet:")
                        print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Client: {client_address[0]}:{client_address[1]}")
                        print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet ID: {data[0]}")
                        print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet Body: {data[1:]}")
                    if data[0] in [ProtocolInfo.OFFLINE_PING, ProtocolInfo.OFFLINE_PING_OPEN_CONNECTIONS]:
                        if config.DEBUG:
                            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet Type: Offline Ping")
                        packet = OfflinePing(data=data)
                        OfflinePingHandler.handle(packet=packet, server=self, connection=client_address)
                    if data[0] == ProtocolInfo.OPEN_CONNECTION_REQUEST_1:
                        if config.DEBUG:
                            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet Type: Open Connection Request 1")
                        packet = OpenConnectionRequest1(data=data)
                        OpenConnectionRequest1Handler.handle(packet, server=self, connection=client_address)
                    if data[0] == ProtocolInfo.OPEN_CONNECTION_REQUEST_2:
                        if config.DEBUG:
                            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet Type: Open Connection Request 2")
                        packet = OpenConnectionRequest2(data=data)
                        OpenConnectionRequest2Handler.handle(packet, server=self, connection=client_address)
                    if data[0] == ProtocolInfo.ACK: #AKC TODO
                        if config.DEBUG:
                            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet Type: ACK")
                        packet: Ack = Ack(data)
                        packet.decode()
                    if data[0] == ProtocolInfo.NACK: #NACK TODO
                        if config.DEBUG:
                            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet Type: ")
                        packet: Nack = Nack(data)
                        packet.decode()
                    if data[0] & ProtocolInfo.FRAME_SET != 0: #Frame set TODO
                        if config.DEBUG:
                            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet Type: FrameSet")
                        packet: FrameSet = FrameSet(data)
                        packet.decode()
                    else:
                        if config.DEBUG:
                            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet Type: Unknown")

            except KeyboardInterrupt:
                print(Fore.RED + text.STOP + Style.RESET_ALL)


if __name__ == "__main__":
    server = PieMC_Server(config.HOST, config.PORT)
    server.start()
