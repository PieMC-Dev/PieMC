from PieMC_Bedrock.packets.login import Login

class LoginHandler:

    def handle(self, frame, connection):
        packet = Login(data=frame.data)

