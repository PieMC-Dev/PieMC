from rak_net.server import server
from packets.game_packet import GamePacket

server = server("0.0.0.0", 19132, 4)


class Interface:
    def __init__(self, server):
        self.server = server
        self.edition = "MCPE"
        self.motd1 = "PieMC-Bedrock"
        self.motd2 = "PieMC-Bedrock"
        self.total_players = 2
        self.max_players = 20
        self.protocol_version = 582
        self.version_name = "1.19.81"
        self.gamemode = "Survival"
        self.gamemode_num = 1
        self.port_v4 = 19132
        self.port_v6 = 19133
        self.server_guid = server.guid
        self.update_server_name()

    def on_frame(self, frame, connection):
        game_packet = GamePacket(frame.body)
        print(f"Новый GamePacket от {connection.address.token}:")
        print(game_packet.data)
        game_packet.decode()
        packets = game_packet.read_packets_data()
        for packet in packets:
            print(f"Новый пакет от {connection.address.token}:")
            print(packet.body)

    def on_disconnect(self, connection):
        print(f"{connection.address.token} отключился.")

    def on_new_incoming_connection(self, connection):
        print(f"{connection.address.token} подключается...")

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

if __name__ == "__main__":
    print("Сервер запущен!")
    while True:
        server.handle()
