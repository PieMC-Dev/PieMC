from piemc.handlers.command import ConsoleCMD

@ConsoleCMD
def ping(server):
    server.logger.info("Pong!")

@ConsoleCMD
def stop(server):
    server.logger.info("Stopping the server...")
    server.stop()

@ConsoleCMD
def setmaxplayers(server, maxplayers):
    server.bedrock_server.max_players = maxplayers
    server.bedrock_server.update_server_status()

@ConsoleCMD
def fakeonline(server, amount):
    server.bedrock_server.players_online = amount
    server.bedrock_server.update_server_status()

