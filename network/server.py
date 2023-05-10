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
        self.game_protocol_version: int = 537
        self.address: tuple = (hostname, port)
        self.guid = random.randint(0, sys.maxsize)
        self.start_time: int = int(time.time() * 1000)
        self.connections: list[Connection] = []
        self.edition: str = "MCPE"
        self.version_name: str = "1.19.81"
        self.player_count: int = 0
        self.max_players: int = 20
        self.handler = PacketHandler(self)

    def add_connection(self, connection: Connection):
        self.connections.append(connection)
    
    def remove_connection(self, connection: Connection):
        i = 0
        for conn in self.connections:
            if conn == connection:
                self.connections.pop(i)
            i += 1

    def run(self):
        while True:
            data, addr = self.recieve()
            self.handler.handle(data, addr) # TODO
