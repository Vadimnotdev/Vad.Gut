from VadGutTitan.Logic.Message.VersionedMessage import VersionedMessage
from VadGutTitan.Logic.DataStream.ByteStream import ByteStream
class SecureConnectionOkMessage(VersionedMessage):
    def  __init__(self):
        super().__init__()
        self.nonce = "nonce"

    def encode(self):
        super().encode()
        self.stream.writeString(self.nonce)

    def getMessageType(self):
        return 20112