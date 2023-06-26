import config
from colorama import Fore
from packets.open_connection_request_1 import OpenConnectionRequest1
from packets.open_connection_reply_1 import OpenConnectionReply1
from ProtocolInfo import ProtocolInfo
from packets.incompatible_protocol_version import IncompatibleProtocolVersion

class OpenConnectionRequest1Handler:
    @staticmethod
    def handle(packet: OpenConnectionRequest1, server, connection: tuple):
        packet: OpenConnectionRequest1 = OpenConnectionRequest1(packet)
        packet.decode()
        if packet.protocol_version == server.protocol_version:
            new_packet: OpenConnectionReply1 = OpenConnectionReply1()
            new_packet.magic = ProtocolInfo.MAGIC
            new_packet.server_guid = server.guid
            new_packet.use_security = False
            new_packet.mtu_size = packet.mtu_size
        else:
            new_packet: IncompatibleProtocolVersion = IncompatibleProtocolVersion()
            new_packet.protocol_version = server.protocol_version
            new_packet.magic = ProtocolInfo.MAGIC
            new_packet.server_guid = server.guid
        new_packet.encode()
        return new_packet.data
