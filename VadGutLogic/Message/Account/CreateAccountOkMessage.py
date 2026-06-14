from VadGutTitan.Logic.Message.VersionedMessage import VersionedMessage
from VadGutTitan.Logic.DataStream.ByteStream import ByteStream
class CreateAccountOkMessage(VersionedMessage):
    def  __init__(self):
        super().__init__()
        self.AccountIdHigherInt = 0
        self.AccountIdLowerInt = 1
        self.SessionKey = ""

    def encode(self):
        super().encode()
        self.stream.writeInt(self.AccountIdHigherInt)
        self.stream.writeInt(self.AccountIdLowerInt)
        self.stream.writeString(self.SessionKey)
        
    def getMessageType(self):
        return 20101