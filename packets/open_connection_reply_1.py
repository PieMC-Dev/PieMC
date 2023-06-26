from packets.packet import Packet


class OpenConnectionReply1(Packet):
    packet_id = 0x06
    magic: bytes = None
    server_guid: int = None
    use_security: bool = None 
    mtu_size: int = None
    
    def decode_payload(self):
        self.write_magic(self.magic)
        self.address = self.write_address()
        self.write_bool(self.use_security)
        self.write("\x00" * self.mtu_size)
