from game_packet import GamePacket

class Disconnect(GamePacket):
    clientbound: bool = False
    serverbound: bool = False

    def __init__(self, data: bytes = b"", pos: int = 0):
        super().__init__(data, pos)
        self.message = None
        self.hide_disconnect_screen = None

    def encode_payload(self):
        self.write_bool(self.hide_disconnect_screen)
        self.write_string(self.message)
