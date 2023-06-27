from packets.packet import Packet


class OpenConnectionReply2(Packet):
    packet_id = 0x08
    magic: bytes = None
    server_guid: int = None
    client_address: tuple = None  # ('255.255.255.255', 19132, 4)
    mtu_size: int = None
    encryption_enabled: bool = None
    
    def encode_payload(self):
        self.write_magic(self.magic)
        self.write_long(self.server_guid)
        self.write_address(self.client_address)
        self.write_short(self.mtu_size)
        self.write_bool(self.encryption_enabled)
