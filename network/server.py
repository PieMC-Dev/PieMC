import time
import sys
import uuid
import random
from PieMC_Bedrock.network.udp_server import UDPServer
from PieMC_Bedrock.network.connection import Connection
from PieMC_Bedrock.handler import PacketHandler

class Server(UDPServer):
    def __init__(self, hostname: str = "0.0.0.0", port: int = 19132):
        super().__init__(hostname, port)
        self.tps: int = 20
        self.tick_sleep_per_time = 1 / self.tps
        self.motd1 = "PieMC-Bedrock"
        self.motd2 = "PieMC-Bedrock"
        self.raknet_version: int = 11
        self.game_protocol_version: int = 582
        self.address: tuple = (hostname, port)
        self.port_v6: int = 19133
        self.gamemode: str = "Survival"
        self.gamemode_num: int = 1
        self.guid = random.randint(1000000000000000, 9999999999999999)
        self.start_time: int = int(time.time() * 1000)
        self.connections: list[Connection] = []
        self.edition: str = "MCPE"
        self.game_version_name: str = "1.19.81"
        self.player_count: int = 0
        self.max_players: int = 20
        self.handler = PacketHandler(self)
        self.name = ";".join([self.edition, self.motd1, str(self.game_protocol_version), self.game_version_name, str(self.player_count), str(self.max_players), str(self.guid), self.motd2, self.gamemode, str(self.gamemode_num), str(self.port), str(self.port_v6)]) + ";"

    def update_name(self):
        self.name = ";".join([self.edition, self.motd1, str(self.game_protocol_version), self.game_version_name, str(self.player_count), str(self.max_players), str(self.guid), self.motd2, self.gamemode, str(self.gamemode_num), str(self.port), str(self.port_v6)]) + ";"

    def add_connection(self, connection: Connection):
        self.connections.append(connection)
    
    def remove_connection(self, connection: Connection):
        i = 0
        for conn in self.connections:
            if conn == connection:
                self.connections.remove(i)
            i += 1

    def run(self):
        while True:
            data, addr = self.recieve()
            self.handler.handle(data, addr)
