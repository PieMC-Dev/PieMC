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
import logging
import os
import random
import socket
import threading
import time

from piemc import config
from piemc.handlers.command import CommandHandler
from piemc.handlers.lang import LangHandler
from pieraknet import Server


class MCBEServer:
    def __init__(self, hostname, port):
        self.lang = LangHandler.initialize_language()
        print(self.lang['INITIALIZING'])
        self.logger = self.create_logger('PieMC')
        if not os.path.exists("pieuid.dat"):
            pieuid = random.randint(10 ** 19, (10 ** 20) - 1)
            with open("pieuid.dat", "w") as uid_file:
                uid_file.write(str(pieuid))
            self.logger.info(f"{self.lang['CREATED_PIEUID']}: {str(pieuid)}")
        self.server_status = None
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.hostname = hostname
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
        print(self.lang['NOT_EXISTING_GAMEMODE'])  if self.gamemode[1] == 0 else None
        self.port = config.PORT
        self.port_v6 = 19133
        self.guid = random.randint(1, 99999999)
        with open('pieuid.dat', 'r') as f:
            pieuid = f.read().strip()
        self.uid = pieuid
        self.raknet_version = 11
        self.timeout = 20
        self.raknet_server = Server(self.hostname, self.port, self.create_logger('PieRakNet'))
        self.raknet_server.interface = self
        self.update_server_status()
        self.raknet_server.name = self.server_status
        self.raknet_server.protocol_version = self.raknet_version
        self.raknet_server.timeout = self.timeout
        # self.raknet_server.magic = ''
        self.raknet_thread = threading.Thread(target=self.raknet_server.start)
        self.raknet_thread.daemon = True
        self.running = False
        self.cmd_handler = CommandHandler(self.create_logger('CMD Handler'))
        self.logger.info(self.lang['SERVER_INITIALIZED'])
        self.start_time = int(time.time())

    def get_time_ms(self):
        return round(time.time() - self.start_time, 4)

    @staticmethod
    def create_logger(name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
    
        log_dir = './log'
        os.makedirs(log_dir, exist_ok=True)  # Create the directory if it doesn't exist
    
        log_file = os.path.join(log_dir, name)
        fhandler = logging.FileHandler(log_file, 'w', 'utf-8')
        shandler = logging.StreamHandler()
    
        formatter = logging.Formatter("[%(name)s]" + str(' ' * (11 - len(name))) + "[%(asctime)s] [%(levelname)s] : %(message)s")
        fhandler.setFormatter(formatter)
        shandler.setFormatter(formatter)
    
        logger.addHandler(fhandler)
        logger.addHandler(shandler)
    
        return logger


    def update_server_status(self):
        self.server_status = ';'.join([
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
        self.raknet_server.name = self.server_status

    def start(self):
        self.running = True
        self.raknet_thread.start()
        self.logger.info(f"{self.lang['RUNNING']} ({self.get_time_ms()}s.)")
        self.logger.info(f"{self.lang['IP']}: {self.hostname}")
        self.logger.info(f"{self.lang['PORT']}: {self.port}")
        self.logger.info(f"{self.lang['GAMEMODE']}: {self.gamemode}")
        self.logger.info(f"{self.lang['MAX_PLAYERS']}: {self.max_players}")
        while self.running:
            cmd = input('>>> ')
            self.cmd_handler.handle_cmd(cmd, self)
            time.sleep(.1)

    def stop(self):
        self.logger.info(self.lang['STOPPING_WAIT'])
        self.running = False
        self.raknet_server.stop()
        self.raknet_thread.join()
        self.logger.info(self.lang['STOP'])


if __name__ == "__main__":
    server = MCBEServer(config.HOST, config.PORT)
    server.start()
