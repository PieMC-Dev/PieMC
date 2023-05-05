from packet import Packet
from ..protocol_info import ProtocolInfo

class ConnectionRequestAccepted(Packet):
    packet_id = ProtocolInfo.CONNECTION_REQUEST_ACCEPTED
    clientbound: bool = True
    serverbound: bool = False
    client_hostname: str = "0.0.0.0"
    client_port: int = 0
    system_index: int = 0
    internal_ids: list = [
        ["255.255.255.255", 19132],
        ["255.255.255.255", 19132],
        ["255.255.255.255", 19132],
        ["255.255.255.255", 19132],
        ["255.255.255.255", 19132],
        ["255.255.255.255", 19132],
        ["255.255.255.255", 19132],
        ["255.255.255.255", 19132],
        ["255.255.255.255", 19132],
        ["255.255.255.255", 19132],
    ]
    request_timestamp: int = 0
    accepted_timestamp: int = 0

    def encode_payload(self):
        self.write_address(client_hostname, client_port)
        self.write_unsigned_short_be(self.system_index)
        for address in self.internal_ids:
            self.write_address(address[0], address[1])
        self.write_unsigned_long_be(self.request_timestamp)
        self.write_unsigned_long_be(self.accepted_timestamp)
