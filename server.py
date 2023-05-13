from rak_net.server import Server

server = Server(11, "0.0.0.0", 19132)


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

    @staticmethod
    def on_frame(frame):
        print(hex(frame.body[0]))

    @staticmethod
    def on_disconnect(connection):
        print(f"{connection.address.token} отключился.")

    @staticmethod
    def on_new_incoming_connection(connection):
        print(f"{connection.address.token} подключается...")

    def update_server_name(self):
        server_name = ";".join([
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
        self.server.name = server_name


server.interface = Interface(server)

if __name__ == "__main__":
    print("Сервер запущен!")
    while True:
        server.handle()
        server.tick()
