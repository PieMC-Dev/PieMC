import config
from colorama import Fore
from packets.open_connection_request_2 import OpenConnectionRequest2
from packets.open_connection_reply_2 import OpenConnectionReply2


class OpenConnectionRequest2Handler:
    @staticmethod
    def handle(packet: OpenConnectionRequest2, server, connection: tuple):
        packet.decode()
        new_packet = OpenConnectionReply2()
        new_packet.magic = packet.magic
        new_packet.server_guid = server.guid
        new_packet.client_address = (connection[0], connection[1], 4)
        new_packet.mtu_size = packet.mtu_size
        new_packet.encode()
        server.send(new_packet.data, connection)
        if config.DEBUG:
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} Sent Packet:")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet ID: {str(new_packet.packet_id)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet Body: {str(new_packet.data[1:])}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet Type: Open Connection Reply 2")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - MAGIC: {str(new_packet.magic)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Server GUID: {str(new_packet.server_guid)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Client Address: {str(new_packet.client_address)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - MTU Size: {str(new_packet.mtu_size)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Encryption Enabled: {str(new_packet.encryption_enabled)}")
