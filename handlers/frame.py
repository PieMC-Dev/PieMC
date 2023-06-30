import config
from colorama import Fore
from packets.frame_set import Frame


class FrameHandler:
    @staticmethod
    def handle(frame: Frame, server, connection: tuple):
        if config.DEBUG:
            debug_info = [
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Frame:",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - - Reliability: {frame.reliability}",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - - Fragmented: {frame.fragmented}",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - - Reliable Frame Index: {frame.reliable_frame_index}",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - - Sequenced Frame Index: {frame.sequenced_frame_index}",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - - Ordered Frame Index: {frame.sequenced_frame_index}",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - - Ordered Frame Index: {frame.order_channel}",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - - Compound Size: {frame.compound_size}",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - - Compound ID: {frame.compound_id}",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - - Index: {frame.index}",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - - Data: {frame.body}",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - - Size: {frame.get_size()}"
            ]
            print("\n".join(debug_info))
