from packet import Packet
from ..protocol_info import ProtocolInfo

class OfflinePing(Packet):
    packet_id = ProtocolInfo.OFFLINE_PING
    clientbound: bool = False
    serverbound: bool = True

    def decode_payload(self):
        self.client_timestamp = self.read_unsigned_long_be()
        self.magic = self.read(16)
        if not self.feos():
            self.client_guid = self.read_unsigned_long_be()
        print(self.client_timestamp)
        print(client_guid)
