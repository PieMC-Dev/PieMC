from pathlib import Path
import config
from server import PieMC_Server

def start_server():
    server = PieMC_Server(config.HOST, config.PORT)
    server.start()

if __name__ == "__main__":
    # Get the current directory of the script
    current_dir = Path(__file__).resolve().parent

    # Start the server
    start_server()
