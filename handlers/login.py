from ..packets.login import Login
from ..packets.disconnect import Disconnect
from ..packets.game_packet import GamePacket
from rak_net.connection import Connection
import config

# Import "en(.py)" or other language from config if defined correctly
with open('languages.txt') as f:
    languages = f.read().strip().split('\n')
    if config.LANG in languages:
        language = config.LANG
    else:
        language = 'en'
text = __import__('lang.' + language, fromlist=[config.LANG])


class LoginHandler:

    def handle(self, packet: GamePacket, connection: Connection):
        login_packet = Login(packet.body)
        login_packet.decode()
        disconnect_packet = Disconnect()
        disconnect_packet.message = text.DISCONNECT_PACKET
        disconnect_packet.hide_disconnect_screen = False
        disconnect_packet.encode()
        connection.send_data(disconnect_packet.data)
