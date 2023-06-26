from packets.packet import Packet


class ConnectionRequestAccepted(Packet):
    packet_id = 0x10
    client_address: bytes = None
    system_index: int = None
    internal_ids: bytes = None
    request_time: int = None
    time: int = None
    def decode_payload(self):
        self.client_address = self.write_address()
        self.write_long(self.system_index)
        self.read_long(self.time)
        self.internal_ids = self.write_packet_id()
        self.write_long(self.request_time)
        self.write_long(self.time)