import config
from colorama import Fore

class OfflinePingHandler:
    @staticmethod
    def handle(packet, server, connection):
        packet.decode()
        if config.DEBUG:
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} Client Timestamp: {str(packet.client_timestamp)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} MAGIC: {str(packet.magic)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} Client GUID: {str(packet.client_guid)}")

    def create_response_packet(self):
        edition = "MCPE"  # DON'T CHANGE
        protocol_version = 589  # DON'T CHANGE
        version_name = "1.20.0"  # DON'T CHANGE
        server_uid = 13253860892328930865  # DON'T CHANGE
        motd1 = config.MOTD1
        motd2 = config.MOTD2
        players_online = 2
        max_players = config.MAX_PLAYERS
        if config.GAMEMODE == "Survival":
            gamemode = "Survival"
            gamemode_num = 0
        elif config.GAMEMODE == "Creative":
            gamemode = "Creative"
            gamemode_num = 1
        elif config.GAMEMODE == "Adventure":
            gamemode = "Adventure"
            gamemode_num = 2
        port_ipv4 = config.PORT
        port_ipv6 = 19133  # NOT NECESSARY

        # response_packet = f"{edition};{motd1};{protocol_version};{version_name};{players_online};{max_players};{server_uid};{motd2};{gamemode};{gamemode_num};{port_ipv4};{port_ipv6};"
        # unconnected_pong = f"2;{response_packet};".encode('utf-8')
        # if config.DEBUG:
        #     print(Fore.BLUE + "[DEBUG] " + Fore.WHITE + "Sent Packet: " + str(response_packet))
        # return unconnected_pong