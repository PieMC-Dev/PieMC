from packets.acknowledgement import Acknowledgement
from ProtocolInfo import ProtocolInfo
from packets.packet import Packet

class Ack(Packet):
    
    packet_id = 0xc0
    record_count: int = None
    record_single_sequence_number: bool = None
    record_start_sequence_number: bytes = None
    record_range_start_sequence_number: bytes = None
    record_range_end_sequence_number: bytes = None
    
    def __init__(self, data: bytes = b"", pos: int = 0):
        super().__init__(data, pos)
        self.packet_id: int = ProtocolInfo.ACK
        
    def encode_payload(self):
        self.record_count
        self.record_single_sequence_number
        self.record_start_sequence_number
        self.record_range_start_sequence_number
        self.record_range_end_sequence_number