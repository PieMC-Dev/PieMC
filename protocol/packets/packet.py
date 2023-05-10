from PieMC_Bedrock.protocol.binary_stream import BinaryStream
from PieMC_Bedrock.protocol.protocol_info import ProtocolInfo

class Packet(BinaryStream):
    packet_id = -1
    clientbound: bool = False
    serverbound: bool = False

    def __init__(self, data: bytes = b"", pos: int = 0):
        super().__init__(data=data, pos=pos)
        self.read_int = self.read_unsigned_int_be
        self.write_int = self.write_unsigned_int_be
        self.read_magic = self.read(16)
        self.write_magic = self.write(ProtocolInfo.MAGIC)
        self.read_long = self.read_unsigned_long_be
        self.write_long = self.write_unsigned_long_be
        self.read_short = self.read_unsigned_long_be
        self.write_short = self.write_unsigned_long_be
        self.read_float = self.read_float_be
        self.write_float = self.write_float_be
        self.read_double = self.read_double_be
        self.write_double = self.write_double_be

    def decode_header(self):
        return self.read(1)

    def encode_header(self):
        self.write_unsigned_byte(self.packet_id)

    def decode(self):
        self.decode_header()
        self.decode_payload()

    def encode(self):
        self.encode_header()
        self.encode_payload()

    def read_string(self):
        length = self.read_unsigned_short_be()
        print(self.data)
        string = self.read(length).decode("utf-8", "ignore")
        return string

    def write_string(self, value: str):
        self.write_unsigned_short_be(len(value))
        self.write(value.encode())

    def read_address(self):
        version: int = self.read_unsigned_byte()
        hostname_parts: list = []
        for i in range(0, 4):
            hostname_parts.append(str(~self.read_unsigned_byte() & 0xff))
        hostname: str = ".".join(hostname_parts)
        port: int = self.read_unsigned_short_be()
        return f"{hostname}:{str(port)}"

    def write_address(self, hostname, port, version=4):
        self.write_unsigned_byte(version)
        hostname_parts: list = hostname.split(".")
        for part in hostname_parts:
            self.write_unsigned_byte(~int(part) & 0xff)
        self.write_unsigned_short_be(address.port)

