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
    server.max_players = maxplayers
    server.update_server_status()

@ConsoleCMD
def fakeonline(server, amount):
    server.players_online = amount
    server.update_server_status()
