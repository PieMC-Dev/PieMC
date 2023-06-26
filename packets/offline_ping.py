from packets.packet import Packet

class OfflinePing(Packet):
    packet_id = 0x01
    client_timestamp: int = None
    magic: bytes = None
    client_guid: int = None

    def read_long(self):
        if len(self.data) < 8:
            raise ValueError("Insufficient data to read a long value")

        long_value = int.from_bytes(self.data[:8], byteorder='big', signed=False)
        self.data = self.data[8:]

        return long_value
    
    def decode_payload(self):
        self.client_timestamp = self.read_long()
        self.magic = self.read_magic()
        self.client_guid = self.read_long()
