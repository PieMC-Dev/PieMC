import config
from colorama import Fore
from packets.offline_ping import OfflinePing
from packets.offline_pong import OfflinePong

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

        if config.DEBUG:
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} Sent Packet:")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet ID: {str(pong.packet_id)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet Body: {str(pong.data[1:])}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet Type: Offline Pong")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Client Timestamp: {str(pong.client_timestamp)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Server GUID: {str(pong.server_guid)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - MAGIC: {str(pong.magic)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Server Name: {str(pong.server_name)}")
