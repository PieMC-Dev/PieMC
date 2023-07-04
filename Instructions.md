# Instructions

## Configuration
> seen here: `server.py` <br>
> line 61 - 72 <br>
> class PieMC_Server: <br>
>    def `__init__`(self, ip, port): <br>
>       self.server_name = None <br>
>       self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) <br>
>       self.ip = ip <br>
>        self.port = port <br>
>        self.edition = "MCPE" <br>
>       self.protocol_version = 589 <br>
>       self.version_name = "1.20.0" <br>
>       self.motd1 = config.MOTD1 <br>
>        self.motd2 = config.MOTD2 <br>
>       self.players_online = 2  # 2 players online XD. Update (By andiri): YES :sunglasses: <br>
>        self.max_players = config.MAX_PLAYERS <br>
