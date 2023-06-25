import config
from colorama import Fore
from packets.offline_pong import OfflinePong
from packets.offline_ping import OfflinePing

class OfflinePingHandler:
    @staticmethod
    def handle(packet: OfflinePing, server, connection: tuple):
        packet.decode()
        if config.DEBUG:
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Client Timestamp: {str(packet.client_timestamp)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - MAGIC: {str(packet.magic)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Client GUID: {str(packet.client_guid)}")

        pong = OfflinePong()

        pong.client_timestamp = packet.client_timestamp
        pong.server_guid = server.guid
        pong.magic = packet.magic

        server.update_server_status()
        pong.server_name = server.server_name

        pong.encode()

        server.send(pong.data, connection)