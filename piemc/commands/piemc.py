from piemc.handlers.command import Command

@Command
def ping(self):
    self.logger.info("Pong!")
    
@Command
def stop(self):
    self.logger.info("Stopping the server...")
    self.stop()

