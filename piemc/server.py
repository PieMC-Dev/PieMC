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
import time

from piemc import config
from piemc.handlers.command import handle_command, initialize_commands
from piemc.handlers.lang import LangHandler
from piemc.handlers.logger import create_logger
from piemc.update import check_for_updates

from piebedrock.server import BedrockServer

class PieServer:
    def __init__(self):
        self.threads = []
        self.running = False
        self.lang = LangHandler.initialize_language()
        self.logger = create_logger('PieMC')
        self.logger.info(self.lang['INITIALIZING'])
        if not os.path.exists("uid.pie"):
            pieuid = random.randint(10 ** 19, (10 ** 20) - 1)
            with open("uid.pie", "w") as uid_file:
                uid_file.write(str(pieuid))
            self.logger.info(f"{self.lang['CREATED_PIEUID']}: {str(pieuid)}")
            
        self.bedrock_server = BedrockServer()
        
        self.cmd_handler = handle_command
        self.logger.info(self.lang['SERVER_INITIALIZED'])
        self.running = True
        self.start_time = int(time.time())
        initialize_commands(self)

    def start(self):
        self.logger.info(f"{self.lang['IP']}: {config.HOST}")
        self.logger.info(f"{self.lang['GAMEMODE']}: {config.GAMEMODE}")
        self.logger.info(f"{self.lang['MAX_PLAYERS']}: {config.MAX_PLAYERS}")
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
        self.logger.info(self.lang['STOP'])


if __name__ == "__main__":
    server = PieServer()
    server.start()

__version__ = "V0.1.0.4" #Github release version (For updates)