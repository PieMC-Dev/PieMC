from PieMC_Bedrock.protocol.protocol_info import ProtocolInfo, GameProtocolInfo
from PieMC_Bedrock.protocol.packets.offline_ping import OfflinePing
from PieMC_Bedrock.protocol.packets.offline_pong import OfflinePong
import time

class PacketHandler:

    def __init__(self, server):
        self.server = server

    def handle(self, data, addr):
        print(f"New packet from {str(addr)}:")
        print(data)
        if data[0] == ProtocolInfo.OFFLINE_PING:
            f = open(f"recieved_packets/OFFLINE_PING_{time.time()}.txt", "w")
            ping = OfflinePing(data=data)
            ping.decode()
            p_data = []
            p_data.append(f"Address: {addr[0]}:{str(addr[1])}")
            p_data.append(f"Packet ID: {str(ping.packet_id)}")
            p_data.append(f"Packet Name: OFFLINE PING")
            p_data.append("")
            p_data.append(f"Packet Data:")
            p_data.append(f"- Client Timestamp: {str(ping.client_timestamp)}")
            p_data.append(f"- Client GUID: {str(ping.client_guid)}")
            p_data.append(f"- MAGIC: {str(ping.magic)}")
            p_data.append("")
            p_data.append(f"Raw:")
            p_data.append(str(ping.data))
            f.write("\n".join(p_data))
            print("Ping saved.")
            pong = OfflinePong()
            pong.client_timestamp = ping.client_timestamp
            pong.server_guid = self.server.guid
            pong.magic = ProtocolInfo.MAGIC
            pong.server_name = self.server.name
            pong.encode()
            self.server.send(pong.data, addr)
            f = open(f"sent_packets/OFFLINE_PONG_{time.time()}.txt", "w")
            p_data = []
            p_data.append(f"Address: {addr[0]}:{str(addr[1])}")
            p_data.append(f"Packet ID: {str(pong.packet_id)}")
            p_data.append(f"Packet Name: OFFLINE PONG")
            p_data.append("")
            p_data.append(f"Packet Data:")
            p_data.append(f"- Client Timestamp: {str(ping.client_timestamp)}")
            p_data.append(f"- Server GUID: {str(pong.server_guid)}")
            p_data.append(f"- MAGIC: {str(pong.magic)}")
            p_data.append(f"- Server Name: {str(pong.server_name)}")
            p_data.append("")
            p_data.append(f"Raw:")
            p_data.append(str(pong.data))
            f.write("\n".join(p_data))
            print("Pong saved.")
        else:
            print(f"Packet {str(data[0])} ignored.")
