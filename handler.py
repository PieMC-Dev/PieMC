from PieMC_Bedrock.protocol.protocol_info import ProtocolInfo, GameProtocolInfo
from PieMC_Bedrock.protocol.packets.offline_ping import OfflinePing
import time

class PacketHandler:

    def __init__(self, server):
        self.server = server

    def handle(self, data, addr):
        print(f"New packet from {str(addr)}:")
        print(data)
        if data[0] == ProtocolInfo.OFFLINE_PING:
            # Packet Logging: OFFLINE PING
            f = open(f"recieved_packets/OFFLINE_PING_{time.time()}.txt", "w")
            packet = OfflinePing(data=data)
            packet.decode()
            p_data = []
            p_data.append(f"Address: {addr[0]}:{str(addr[1])}")
            p_data.append(f"Packet ID: {str(packet.packet_id)}")
            p_data.append(f"Packet Name: OFLINE PING")
            p_data.append("")
            p_data.append(f"Packet Data:")
            p_data.append(f"- Client Timestamp: {str(packet.client_timestamp)}")
            p_data.append(f"- Client GUID: {str(packet.client_guid)}")
            p_data.append(f"- MAGIC: {str(packet.magic)}")
            p_data.append("")
            p_data.append(f"Raw:")
            p_data.append(str(packet.data))
            f.write("\n".join(p_data))
        else:
            print(f"Packet {str(data[0])} ignored.")
