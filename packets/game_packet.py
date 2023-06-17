from binary_utils.binary_stream import binary_stream
from rak_net.protocol.packet import packet
import zlib

class GamePacket(packet):
    clientbound: bool = None
    serverbound: bool = None
    packet_id = 0xfe

    def __init__(self, data: bytes = b"", pos: int = 0):
        super().__init__(data, pos)
        self.body = None

    def decode_payload(self):
        try:
            self.body = zlib.decompress(self.read_remaining(), -zlib.MAX_WBITS, 1024 * 1024 * 8)
        except BaseException as error:
            print(repr(error))
            self.body = self.read_remaining()

    def encode_payload(self):
        compress = zlib.compressobj(1, zlib.DEFLATED, -zlib.MAX_WBITS)
        compressed_data = compress.compress(self.body)
        compressed_data += compress.flush()
        self.write(compressed_data)

    def write_packet_data(self, data):
        buffer = binary_stream()
        buffer.write_var_int(len(data))
        buffer.write(data)
        if hasattr(self, "body"):
            self.body += buffer.data
        else:
            self.body = buffer.data

    def read_packets_data(self):
        buffer = binary_stream(self.body)
        packets_data = []
        while not buffer.feos():
            packets_data.append(packets_data.append(buffer.read(buffer.read_var_int())))
        return packets_data
