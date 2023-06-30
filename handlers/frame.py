import config
from colorama import Fore
from packets.frame_set import Frame


class FrameHandler:
    @staticmethod
    def handle(frame: Frame, server, connection: tuple):
        if config.DEBUG:
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Frame:")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - - Reliability: {str(frame.reliability)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - - Fragmented: {str(frame.fragmented)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - - Reliable Frame Index: {str(frame.reliable_frame_index)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - - Sequenced Frame Index: {str(frame.sequenced_frame_index)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - - Ordered Frame Index: {str(frame.sequenced_frame_index)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - - Ordered Frame Index: {str(frame.order_channel)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - - Compound Size: {str(frame.compound_size)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - - Compound ID: {str(frame.compound_id)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - - Index: {str(frame.index)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - - Data: {str(frame.body)}")
            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - - Size: {str(frame.get_size())}")
