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
import piemc.handlers.command
from piemc.meta.protocol_info import ProtocolInfo
from piemc.update import check_for_updates

from piebedrock.server import BedrockServer

class PieServer:
    def __init__(self, hostname="0.0.0.0", port=19132, name="PieMC Server", motd="Powered by PieMC", version_name="1.20.12",
                 protocol_version=594, max_players=20, gamemode="survival", guid=random.randint(1, 99999999),
                 raknet_version=11, timeout=20):
        self.threads = []
        self.lang = LangHandler.initialize_language()
        self.logger = create_logger('PieMC')
        self.logger.info(self.lang['INITIALIZING'])

        if not os.path.exists("pieuid.dat"):
            pieuid = random.randint(10 ** 19, (10 ** 20) - 1)
            with open("pieuid.dat", "w") as uid_file:
                uid_file.write(str(pieuid))
            self.logger.info(f"{self.lang['CREATED_PIEUID']}: {str(pieuid)}")
        with open('pieuid.dat', 'r') as f:
            pieuid = f.read().strip()

        self.logger.info(self.lang['NOT_EXISTING_GAMEMODE']) if gamemode[1] == 0 else None

        self.hostname = hostname
        self.port = port
        self.port_v6 = 19133
        self.guid = random.randint(1, 99999999)
        self.raknet_version = 11
        self.timeout = 20
        self.uid = pieuid
        self.gamemode = gamemode
        self.max_players = max_players
        self.dev_mode = config.DEV_MODE

        self.bedrock_server = BedrockServer()
        self.bedrock_server.hostname = hostname
        self.bedrock_server.port = port
        self.bedrock_server.gamemode = gamemode
        self.bedrock_server.protocol_version = protocol_version
        self.bedrock_server.version_name = version_name
        self.bedrock_server.name = name
        self.bedrock_server.motd = motd
        self.bedrock_server.max_players = max_players
        self.bedrock_server.uid = pieuid
        self.bedrock_server.guid = guid
        self.bedrock_server.raknet_version = raknet_version

        self.bedrockServer_thread = threading.Thread(target=self.start_bedrock_server)
        self.bedrockServer_thread.daemon = True
        self.threads.append(self.bedrockServer_thread)

        self.running = False
        self.cmd_handler = handle_command
        self.logger.info(self.lang['SERVER_INITIALIZED'])
        self.start_time = int(time.time())
        initialize_commands(piemc.handlers.command)

    def start_bedrock_server(self):
        try:
            self.bedrock_server.start()
        except Exception as e:
            self.logger.error(f"Error during Bedrock server start: {e}")

    def get_time_ms(self):
        return round(time.time() - self.start_time, 4)

    def start(self):
        try:
            self.bedrockServer_thread.start()
            self.running = True
            self.logger.info(f"{self.lang['RUNNING']} ({self.get_time_ms()}s.)")
            self.logger.info(f"{self.lang['IP']}: {self.hostname}")
            self.logger.info(f"{self.lang['PORT']}: {self.port}")
            self.logger.info(f"{self.lang['GAMEMODE']}: {self.gamemode}")
            self.logger.info(f"{self.lang['MAX_PLAYERS']}: {self.max_players}")
            self.logger.info(f"\033[36m{self.lang['NEEDHELP?']}\033[0m")
            self.logger.info(f"\033[36m{self.lang['DISCORDINVITE']}\033[0m")
            # try:
            #    check_for_updates()
            #except Exception as e:
            #    self.logger.error(f"Error while checking for updates: {e}")
            while self.running:
                cmd = input('>>> ')
                self.cmd_handler(self, cmd)
        except Exception as e:
            self.logger.error(f"Error during start: {e}")

    def stop(self):
        self.logger.info(self.lang['STOPPING_WAIT'])
        self.running = False
        self.bedrock_server.stop()
        for thread in self.threads:
            thread.join()
        self.logger.info(self.lang['STOP'])


if __name__ == "__main__":
    server = PieServer(hostname=config.HOST, port=config.PORT)
    server.start()
