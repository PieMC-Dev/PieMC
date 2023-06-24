import config
from colorama import Fore
from packets.offline_pong import OfflinePong
from packets.offline_ping import OfflinePing
from server import PieMC_Server


class OfflinePingHandler:
    def handle(self, packet: OfflinePing, server: PieMC_Server, connection: tuple):
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