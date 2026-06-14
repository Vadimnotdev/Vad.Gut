from VadGutTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from VadGutTitan.Logic.DataStream.ByteStream import ByteStream
class VersionedMessage(PiranhaMessage):
    def __init__(self):
        super().__init__(0)
        self.version = 0


    def encode(self):
        self.stream.writeInt(self.version)
    
    def decode(self):
        self.version = self.stream.readInt()

    
    def setVersion(self, major, build, minor):
        self.version = minor | (major << 20) | (build << 12)