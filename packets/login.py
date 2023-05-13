import json
from binary_utils.binary_stream import BinaryStream
from game_packet import GamePacket
from .. import jwt


class Login(GamePacket):
    clientbound: False
    serverbound: True

    def __init__(self, data: bytes = b"", pos: int = 0):
        super().__init__(data, pos)
        self.skin_data = None
        self.chain_data = None
        self.protocol_version = None

    def decode_payload(self):
        self.protocol_version = self.read_unsigned_int_be()
        self.chain_data = []
        buffer = BinaryStream(self.read_byte_array())
        raw_chain_data = json.loads(buffer.read(buffer.read_unsigned_int_le()).decode())
        for chain in raw_chain_data["chain"]:
            self.chain_data.append(jwt.decode(chain))
            self.skin_data: dict = jwt.decode(buffer.read(buffer.read_unsigned_int_le()).decode())

    def encode_payload(self):
        self.write_unsigned_int_be(self.protocol_version)
        raw_chain_data = {"chain": []}
        for chain in self.chain_data:
            jwt_data = jwt.encode({"alg": "HS256", "typ": "JWT"}, chain, jwt.mojang_public_key)
            raw_chain_data["chain"].append(jwt_data)
        temp_stream = BinaryStream()
        json_data = json.dumps(raw_chain_data)
        temp_stream.write_unsigned_int_le(len(json_data))
        temp_stream.write(json_data.encode())
        self.write_byte_array(temp_stream.data)
        jwt_data = jwt.encode({"alg": "HS256", "typ": "JWT"}, self.skin_data, jwt.mojang_public_key)
        self.write_unsigned_int_le(len(jwt_data))
        self.write(jwt_data.encode())
