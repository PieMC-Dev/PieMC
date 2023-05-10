from PieMC_Bedrock.protocol.packets.packet import Packet
from PieMC_Bedrock.protocol.protocol_info import ProtocolInfo

class Disconnect(Packet):
    packet_id = ProtocolInfo.DISCONNECT
    clientbound: bool = True
    serverbound: bool = True
