from PieMC_Bedrock.network.server import Server

server = Server()

if __name__ == "__main__":
    try:
        server.run()
    except KeyboardInterrupt:
        print("\nQuit.")
