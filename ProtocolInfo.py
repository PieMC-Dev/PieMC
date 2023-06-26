class ProtocolInfo:
    # RakNet Offline Message ID
    MAGIC: bytes = b"\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78"
    # RakNet Packet IDs
    ONLINE_PING: int = 0x00
    OFFLINE_PING: int = 0x01
    OFFLINE_PING_OPEN_CONNECTIONS: int = 0x02
    ONLINE_PONG: int = 0x03
    OPEN_CONNECTION_REQUEST_1: int = 0x05
    OPEN_CONNECTION_REPLY_1: int = 0x06
    OPEN_CONNECTION_REQUEST_2: int = 0x07
    OPEN_CONNECTION_REPLY_2: int = 0x08
    CONNECTION_REQUEST: int = 0x09
    CONNECTION_REQUEST_ACCEPTED: int = 0x10
    NEW_INCOMING_CONNECTION: int = 0x13
    DISCONNECT: int = 0x15
    INCOMPATIBLE_PROTOCOL_VERSION: int = 0x19
    OFFLINE_PONG: int = 0x1c
    FRAME_SET: int = 0x80
    NACK: int = 0xa0
    ACK: int = 0xc0