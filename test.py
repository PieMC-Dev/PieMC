from PieMC_Bedrock.protocol.packets.offline_pong import OfflinePong
from PieMC_Bedrock.protocol.protocol_info import ProtocolInfo

packet = OfflinePong()
packet.client_timestamp = 18302063724077536888
packet.server_guid = 9738771886805978
packet.magic = b'\xbe\xaf\xcc\xa6\xa6\xdc\x04\xea\x00\xff\xff\x00\xfe\xfe\xfe\xfe'
packet.server_name = "MCPE;Dedicated Server;390;1.14.60;0;10;13253860892328930865;Bedrock level;Survival;1;19132;19133;"
packet.encode()
packet.decode()
print(packet.magic)
print(packet.client_timestamp)
print(packet.server_guid)
print(packet.server_name)
