import config
from colorama import Fore
from packets.frame_set import FrameSet
from handlers.frame import FrameHandler


class FrameSetHandler:
    @staticmethod
    def handle(packet: FrameSet, server, connection: tuple):
        packet.decode()
        if config.DEBUG:
            debug_info = [
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Sequence Number: {packet.sequence_number}",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Size: {packet.get_size()}",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Frames:"
            ]
            for frame in packet.frames:
                debug_info.append(FrameHandler.handle(frame, server, connection))
            print("\n".join(debug_info))