from ..buffer import Buffer


class Packet(Buffer):
    packet_id = 0x00
    def decode_header(self):
        return self.read_byte()

    def encode_header(self):
        self.write_byte(self.packet_id)

    def decode(self):
        self.decode_header()
        if hasattr(self, 'decode_payload'):
            self.decode_payload()

    def encode(self):
        self.encode_header()
        if hasattr(self, 'encode_payload'):
            self.encode_payload()
