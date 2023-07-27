from piemc.handlers.lang import LangHandler


class CommandHandler:
    def __init__(self, logger):
        self.logger = logger

    def handle(self, cmd, server):
        self.lang = LangHandler.initialize_language()
        if cmd == 'stop':
            self.handle_stop_cmd(server)
        elif cmd == 'restart':
            self.handle_restart_cmd(server)
        elif cmd == '':
            print(self.lang['EMPTY_COMMAND'])
        else:
            print(self.lang['NOT_A_COMMAND'].format(cmd))

    def handle_stop_cmd(self, server):
        self.logger.info(self.lang['STOPPING'])
        server.stop()

    def handle_restart_cmd(self, server):
        self.logger.info(self.lang['RESTARTING'])
        self.logger.error('This command in development now')
        # server.stop()
        # server.start()
