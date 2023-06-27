from packets.packet import Packet


class ConnectionRequestAccepted(Packet):
    packet_id = 0x10
    client_address: tuple = None  # ('255.255.255.255', 19132, 4)
    system_index: int = None  # Unknown, 0 works
    internal_ids: list = None  # list of 10 addresses
    request_timestamp: int = None
    accepted_timestamp: int = None

    def encode_payload(self):
        self.write_address(self.client_address)
        self.write_short(self.system_index)
        for address in self.internal_ids:
            self.write_address(address)
        self.write_long(self.request_timestamp)
        self.write_long(self.accepted_timestamp)
