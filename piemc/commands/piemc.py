from piemc.handlers.command import Command


@Command
def ping(server):
    server.logger.info("Pong!")


@Command
def stop(server):
    server.logger.info("Stopping the server...")
    server.stop()

@Command
def setmaxplayers(server, maxplayers):
    server.max_players = maxplayers
    server.update_server_status()

@Command
def fakeonline(server, fakeonline):
    server.players_online = fakeonline
    server.update_server_status()
