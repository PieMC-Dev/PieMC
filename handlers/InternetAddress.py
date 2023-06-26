class InternetAddress:
    def __init__(self, hostname: str, port: int, version: int = 4) -> None:
        self.hostname: str = hostname
        self.port: int = port
        self.version: int = version
        self.token: str = f"{hostname}:{port}"