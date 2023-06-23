import os, sys

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the current directory to sys.path
sys.path.append(current_dir)

from server import MinecraftBedrockServer
import config

if __name__ == "__main__":
    server = MinecraftBedrockServer(config.HOST, config.PORT)
    server.start()