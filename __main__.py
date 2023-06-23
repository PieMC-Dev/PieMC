from server import MinecraftBedrockServer
import config

if __name__ == "__main__":
    server = MinecraftBedrockServer(config.HOST, config.PORT)
    server.start()