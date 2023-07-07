class CommandHandler:
    def __init__(self, logger):
        self.logger = logger

    def handle_cmd(self, cmd, server):
        if cmd == 'stop':
            self.handle_stop_cmd(server)
        elif cmd == 'restart':
            self.handle_restart_cmd(server)

    def handle_stop_cmd(self, server):
        self.logger.info('Stopping...')
        server.stop()

    def handle_restart_cmd(self, server):
        self.logger.info('Restarting...')
        self.logger.error('This command in development now')
        # server.stop()
        # server.start()
