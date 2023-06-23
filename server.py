import socket
import config
import random
import os
from colorama import Fore, Style
import time
from packets.offline_ping import OfflinePing
from handlers.offline_ping import OfflinePingHandler

lang_dirname = "lang"
file_to_find = config.LANG + ".py"

lang_fullpath = os.path.join(os.getcwd(), 'PieMC', lang_dirname)

if os.path.exists(lang_fullpath):
    lang_path = os.path.join(lang_fullpath, file_to_find)
    if os.path.isfile(lang_path):
        language = config.LANG
    else:
        language = 'en'
        print(f"The {config.LANG} lang doesn't exist in the {lang_dirname} directory. Using English...")
        time.sleep(5)

text = __import__('lang.' + language, fromlist=[config.LANG])

if not os.path.exists("server.key"):
    pieuid = random.randint(10**19, (10**20)-1)
    with open("server.key", "w") as key_file:
        key_file.write(str(pieuid))
    print("Created server.key and added pieuid:", pieuid)

class MinecraftBedrockServer:
    def __init__(self, ip, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ip = ip
        self.port = port

    def send(self, data, connection):
        self.socket.sendto(data, connection)

    def start(self):
        with self.socket as server_socket:
            server_socket.bind((self.ip, self.port))
            self.socket = server_socket
            print(Fore.GREEN + Style.BRIGHT + "Server started!" + Style.RESET_ALL)
            print(f"{text.IP}: {Fore.YELLOW}{config.HOST}{Style.RESET_ALL}")
            print(f"{text.PORT}: {Fore.YELLOW}{config.PORT}{Style.RESET_ALL}")
            print(f"{text.GAMEMODE}: {Fore.YELLOW}{config.GAMEMODE}{Style.RESET_ALL}")
            print(f"{text.MAX_PLAYERS}: {Fore.YELLOW}{config.MAX_PLAYERS}{Style.RESET_ALL}")

            try:
                while True:
                    data, client_address = server_socket.recvfrom(1024)
                    if config.DEBUG:
                        print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} New packet:")
                        print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet ID: {data[0]}")
                        print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} Packet Body: {data[1:]}")
                    if data[0] == 0x01:
                        if config.DEBUG:
                            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} Packet Type: ")
                        packet = OfflinePing(data=data)
                        OfflinePingHandler.handle(packet=packet, server=self, connection=client_address)
                    else:
                        if config.DEBUG:
                            print(f"{Fore.BLUE}[DEBUG]{Fore.WHITE} Packet Type: Unknown")

            except KeyboardInterrupt:
                print(Fore.RED + "Server stopped." + Style.RESET_ALL)

if __name__ == "__main__":
    server = MinecraftBedrockServer(config.HOST, config.PORT)
    server.start()
