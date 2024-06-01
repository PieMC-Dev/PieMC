from piemc.server import PieServer
from piemc.handlers.events import EVENT


class Context:
    def __init__(self, server: PieServer):
        """
        Base context class.
        :param server: The server instance.
        """
        self.server = server


class EventContext(Context):
    def __init__(self, server: PieServer, event: EVENT):
        """
        Context related to a server event.
        :param server: The server instance.
        :param event: The event that was triggered.
        """
        super().__init__(server)
        self.event = event
