from rak_net.server import server as raknet_server
from packets.game_packet import GamePacket
import config

# Import "en(.py)" or other language from config if defined correctly
with open('languages.txt') as f:
    languages = f.read().strip().split('\n')
    if config.LANG in languages:
        language = config.LANG
    else:
        language = 'en'
text = __import__('lang.' + language, fromlist=[config.LANG])

server = raknet_server("0.0.0.0", 19132, 4)

class Interface:
    def __init__(self, server):
        self.server = server
        self.edition = "MCPE"
        self.motd1 = config.MOTD1
        self.motd2 = config.MOTD2
        self.total_players = 2
        self.max_players = config.MAX_PLAYERS  # Use the configuration variable from config.py
        self.protocol_version = config.PROTOCOL_VERSION
        self.version_name = config.VERSION_NAME
        self.gamemode = config.GAMEMODE
        self.gamemode_num = config.GAMEMODE_NUM
        self.port_v4 = config.PORT_V4
        self.port_v6 = config.PORT_V6
        self.server_guid = server.guid
        self.update_server_name()

    def on_frame(self, frame, connection):
        game_packet = GamePacket(frame.body)
        # print(f"{text.NEWPACKET} {connection.address.token}:")
        print(game_packet.data)
        game_packet.decode()
        packets = game_packet.read_packets_data()
        for packet in packets:
            print(f"{text.NEWPACKET} {connection.address.token}:")
            print(packet.body)

    def on_disconnect(self, connection):
        print(f"{connection.address.token} {text.DISCONNECTED}")

    def on_new_incoming_connection(self, connection):
        print(f"{connection.address.token} {text.CONNECTING}")

    def update_server_name(self):
        self.server.name = ";".join([
            self.edition,
            self.motd1,
            str(self.protocol_version),
            self.version_name,
            str(self.total_players),
            str(self.max_players),
            str(self.server_guid),
            self.motd2,
            self.gamemode,
            str(self.gamemode_num),
            str(self.port_v4),
            str(self.port_v6)
        ]) + ";"

server.interface = Interface(server)

def run():
    print(text.RUNNING)
    while True:
        server.handle()

if __name__ == '__main__':
    run()