from ..packets.login import Login
from ..packets.disconnect import Disconnect
from ..packets.game_packet import GamePacket
from rak_net.connection import Connection


class LoginHandler:
    @staticmethod
    def handle(packet: GamePacket, connection: Connection):
        login_packet = Login(packet.body)
        login_packet.decode()
        disconnect_packet = Disconnect()
        disconnect_packet.message = "PieMC-Bedrock is not done.\nWe are work on it day and night.\nIf you are want " \
                                    "to help us, you can contribute:\nhttps://github.com/LapisMYT/PieMC_Bedrock"
        disconnect_packet.hide_disconnect_screen = False
        disconnect_packet.encode()
        connection.send_data(disconnect_packet.data)
