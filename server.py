import socket
import config
import random
import os
from colorama import Fore, Style
import time
from packets.packet import Packet
from packets.offline_ping import OfflinePing

lang_dirname = "lang"
file_to_find = config.LANG + ".py"

lang_fullpath = os.path.join(os.getcwd(), lang_dirname)

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
        self.ip = ip
        self.port = port

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
            server_socket.bind((self.ip, self.port))
            print(Fore.GREEN + Style.BRIGHT + "Server started!" + Style.RESET_ALL)
            print(f"{text.IP}: {Fore.YELLOW}{config.HOST}{Style.RESET_ALL}")
            print(f"{text.PORT}: {Fore.YELLOW}{config.PORT}{Style.RESET_ALL}")
            print(f"{text.GAMEMODE}: {Fore.YELLOW}{config.GAMEMODE}{Style.RESET_ALL}")
            print(f"{text.MAX_PLAYERS}: {Fore.YELLOW}{config.MAX_PLAYERS}{Style.RESET_ALL}")

            try:
                while True:
                    data, client_address = server_socket.recvfrom(1024)
                    packet = f

                    # Send a response packet to the client
                    response_packet = self.create_response_packet()
                    server_socket.sendto(response_packet, client_address)

            except KeyboardInterrupt:
                print(Fore.RED + "Server stopped." + Style.RESET_ALL)

    @staticmethod
    def create_response_packet():
        edition = "MCPE"  # DON'T CHANGE
        protocol_version = 589  # DON'T CHANGE
        version_name = "1.20.0"  # DON'T CHANGE
        server_uid = 13253860892328930865  # DON'T CHANGE
        motd1 = config.MOTD1
        motd2 = config.MOTD2
        players_online = 2
        max_players = config.MAX_PLAYERS
        if config.GAMEMODE == "Survival":
            gamemode = "Survival"
            gamemode_num = 0
        elif config.GAMEMODE == "Creative":
            gamemode = "Creative"
            gamemode_num = 1
        elif config.GAMEMODE == "Adventure":
            gamemode = "Adventure"
            gamemode_num = 2
        port_ipv4 = config.PORT
        port_ipv6 = 19133  # NOT NECESSARY

        response_packet = f"{edition};{motd1};{protocol_version};{version_name};{players_online};{max_players};{server_uid};{motd2};{gamemode};{gamemode_num};{port_ipv4};{port_ipv6};"
        unconnected_pong = f"2;{response_packet};".encode('utf-8')
        if config.DEBUG:
            print(Fore.BLUE + "[DEBUG] " + Fore.WHITE + "Sent Package: " + str(response_packet))
        return unconnected_pong


if __name__ == "__main__":
    server = MinecraftBedrockServer(config.HOST, config.PORT)
    server.start()
