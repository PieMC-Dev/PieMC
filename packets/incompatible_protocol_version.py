from packets.packet import Packet


class IncompatibleProtocolVersion(Packet):
    packet_id = 0x19
    raknet_version: int = None
    magic: bytes = None
    server_guid: int = None

    def encode_payload(self):
        self.write_byte(self.raknet_version)
        self.write_magic(self.magic)
        self.write_long(self.server_guid)
