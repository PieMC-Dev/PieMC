import config
from colorama import Fore
from packets.frame_set import FrameSet
from packets.frame_set import Frame
from handlers.frame import FrameHandler


class FrameSetHandler:
    @staticmethod
    def handle(packet: FrameSet, server, connection: tuple):
        packet.decode()
        if config.DEBUG:
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Sequence Number: {str(packet.sequence_number)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Size: {str(packet.get_size())}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Frames:")
            for frame in packet.frames:
                FrameHandler.handle(frame, server, connection)
