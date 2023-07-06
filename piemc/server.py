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
from piemc import config
from piemc.meta.protocol_info import ProtocolInfo
import random
import os
import time

# from packets.acknowledgement import Ack
# from packets.acknowledgement import Nack

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

    def start(self):
        pass


if __name__ == "__main__":
    server = PieMC_Server(config.HOST, config.PORT)
    server.start()
