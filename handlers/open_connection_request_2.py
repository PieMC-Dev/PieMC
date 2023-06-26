import config
from colorama import Fore
from ProtocolInfo import ProtocolInfo
from packets.open_connection_request_2 import OpenConnectionRequest2
from packets.open_connection_reply_2 import OpenConnectionReply2

class OpenConnectionRequest2Handler:
    @staticmethod
    def handle(packet: OpenConnectionRequest2, server, connection: tuple):
        packet: OpenConnectionRequest2 = OpenConnectionRequest2(packet)
        packet.decode()
        new_packet: OpenConnectionReply2 = OpenConnectionReply2()
        new_packet.magic = ProtocolInfo.MAGIC
        new_packet.server_guid = server.guid
        new_packet.client_address = connection # connection = address TODO Implement or edit
        new_packet.mtu_size = packet.mtu_size
        new_packet.encription_enabled = False
        new_packet.encode()
        server.add_connection(connection, packet.mtu_size) # connection = address TODO Implement or edit
        return new_packet.data
