# -*- coding: utf-8 -*-

#  ____  _      __  __  ____
# |  _ \(_) ___|  \/  |/ ___|
# | |_) | |/ _ \ |\/| | |
# |  __/| |  __/ |  | | |___
# |_|   |_|\___|_|  |_|\____|
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# @author PieMC Team
# @link http://www.PieMC-Dev.github.io/

import os
import random
import threading
import time

from piemc import config
from piemc.handlers.command import handle_command, initialize_commands
from piemc.handlers.lang import LangHandler
from piemc.handlers.logger import create_logger
from piemc.meta.protocol_info import ProtocolInfo
import piemc.commands
from piemc.update import check_for_updates

from pieraknet import Server
from pieraknet.packets.game_packet import GamePacket
from pieraknet.packets.frame_set import Frame
from pieraknet.connection import Connection


class MCBEServer:
    def __init__(self, hostname, port):
        self.threads = []
        self.lang = LangHandler.initialize_language()
        self.logger = create_logger('PieMC')
        self.logger.info(self.lang['INITIALIZING'])
        if not os.path.exists("pieuid.dat"):
            pieuid = random.randint(10 ** 19, (10 ** 20) - 1)
            with open("pieuid.dat", "w") as uid_file:
                uid_file.write(str(pieuid))
            self.logger.info(f"{self.lang['CREATED_PIEUID']}: {str(pieuid)}")
        self.server_status = None
        self.hostname = hostname
        self.edition = "MCPE"
        self.protocol_version = 594
        self.version_name = "1.20.12"
        self.motd = config.MOTD
        self.level = "Powered by PieMC"
        self.players_online = 2  # 2 players online XD. Update (By andiri): YES :sunglasses:
        self.max_players = config.MAX_PLAYERS
        self.gamemode_map = {
            "survival": ("Survival", 1),
            "creative": ("Creative", 2),
            "adventure": ("Adventure", 3)
        }
        self.gamemode = self.gamemode_map.get(config.GAMEMODE.lower(), ("Survival", 0))
        self.logger.info(self.lang['NOT_EXISTING_GAMEMODE']) if self.gamemode[1] == 0 else None
        self.port = config.PORT
        self.port_v6 = 19133
        self.guid = random.randint(1, 99999999)
        with open('pieuid.dat', 'r') as f:
            pieuid = f.read().strip()
        self.uid = pieuid
        self.raknet_version = 11
        self.timeout = 20
        self.raknet_server = Server(self.hostname, self.port, create_logger('PieRakNet'))
        self.raknet_server.interface = self
        self.update_server_status()
        self.raknet_server.protocol_version = self.raknet_version
        self.raknet_server.timeout = self.timeout
        # self.raknet_server.magic = ''
        self.raknet_thread = threading.Thread(target=self.raknet_server.start)
        self.raknet_thread.daemon = True
        self.threads.append(self.raknet_thread)
        self.running = False
        self.cmd_handler = handle_command
        self.logger.info(self.lang['SERVER_INITIALIZED'])
        self.start_time = int(time.time())
        initialize_commands(piemc.handlers.command)
        
    def get_time_ms(self):
        return round(time.time() - self.start_time, 4)

    def update_server_status(self):
        self.server_status = ";".join([
            self.edition,
            self.motd,
            f"{self.protocol_version}",
            self.version_name,
            f"{self.players_online}",
            f"{self.max_players}",
            f"{self.uid}",
            self.level,
            self.gamemode[0],
            f"{self.gamemode[1]}",
            f"{self.port}",
            f"{self.port_v6}"
        ]) + ";"
        self.raknet_server.name = self.server_status

    def on_game_packet(self, packet: GamePacket, connection: Connection):
        packet.decode()
        if packet.body[0] == ProtocolInfo.LOGIN:
            self.logger.info(f"New Login Packet: {str(packet.body)}")

    def on_new_incoming_connection(self, connection: Connection):
        self.logger.info(f"New Incoming Connection: {str(connection.address)}")

    def on_disconnect(self, connection: Connection):
        self.logger.info(f"{str(connection.address)} disconnected")

    def on_unknown_packet(self, packet: Frame, connection: Connection):
        self.logger.info(f"New Unknown Packet: {str(packet.body)}")

    def start(self):
        self.running = True
        self.raknet_thread.start()
        self.logger.info(f"{self.lang['RUNNING']} ({self.get_time_ms()}s.)")
        self.logger.info(f"{self.lang['IP']}: {self.hostname}")
        self.logger.info(f"{self.lang['PORT']}: {self.port}")
        self.logger.info(f"{self.lang['GAMEMODE']}: {self.gamemode}")
        self.logger.info(f"{self.lang['MAX_PLAYERS']}: {self.max_players}")
        self.logger.info(f"\033[36m{self.lang['NEEDHELP?']}\033[0m")
        self.logger.info(f"\033[36m{self.lang['DISCORDINVITE']}\033[0m")
        try:
            check_for_updates()
        except:
            self.logger.error("Error while checking for updates")
        while self.running:
            cmd = input('>>> ')
            self.cmd_handler(self, cmd)
            
    def stop(self):
        self.logger.info(self.lang['STOPPING_WAIT'])
        self.running = False
        self.raknet_server.stop()
        self.raknet_thread.join()
        self.logger.info(self.lang['STOP'])


if __name__ == "__main__":
    server = MCBEServer(config.HOST, config.PORT)
    server.start()
