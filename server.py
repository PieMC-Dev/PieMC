from rak_net.connection import Connection
from rak_net.server import Server
from rak_net.protocol.packet.frame import Frame

server = Server(10, "0.0.0.0", 19132)

edition = "MCPE"
motd1 = "PieMC-Bedrock"
motd2 = "PieMC-Bedrock"
total_players = 2
max_players = 20
protocol_version = 582
version_name = "1.19.81"
gamemode = "Survival"
gamemode_num = 1
port_v4 = 19132
port_v6 = 19133
server_guid = server.guid

server.name = ";".join([
        edition,
        motd1,
        str(protocol_version),
        version_name,
        str(total_players),
        str(max_players),
        str(server_guid),
        motd2,
        gamemode,
        str(gamemode_num),
        str(port_v4),
        str(port_v6)
    ]) + ";"

class Interface:
    def __init__(self, server):
        self.server = server
    
    def on_frame(self, frame, connection):
        print(hex(frame.body[0]))

    def on_disconnect(self, connection):
        print(f"{connection.address.token} отключился.")

    def on_new_incoming_connection(self, connection):
        print(f"{connection.address.token} подключается...")

    def update_server_name(self):
        server_name = ";".join([
            edition,
            motd1,
            protocol_version,
            version_name,
            total_players,
            max_players,
            server_guid,
            motd2,
            gamemode,
            gamemode_num,
            port_v4,
            port_v6
        ]) + ";"
        self.server.name = server_name

server.interface = Interface(server)

if __name__ == "__main__":
    print("Сервер запущен!")
    while True:
        server.handle()
        server.tick()
