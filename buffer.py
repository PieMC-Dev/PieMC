from io import BytesIO

# Please not use this now, it's very raw
class Buffer:
    def __init__(data, pos=0):
      # data is bytes: b'qwe123'
      self.data = data
      self.pos = pos
      
    def write(data):
      self.data += data
      self.pos += len(data)
      
    def read(length):
      self.pos += length
      return # TODO
