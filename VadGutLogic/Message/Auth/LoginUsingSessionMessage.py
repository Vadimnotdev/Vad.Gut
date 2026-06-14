from VadGutTitan.Logic.Message.VersionedMessage import VersionedMessage
from VadGutTitan.Logic.Math.LogicLong import LogicLong
class LoginUsingSessionMessage(VersionedMessage):
    def __init__(self):
        super().__init__()
        self.AccountId = LogicLong(0, 1)
        self.ClientGameVersion = 0
        self.SessionKey = ""
        self.GamecenterId = ""

    def decode(self):
        super().decode()
        self.AccountId = self.stream.readLong()
        self.ClientGameVersion = self.stream.readInt()
        self.stream.readInt()
        self.SessionKey = self.stream.readString()
        self.stream.readString()
        self.stream.readString()
        self.GamecenterId = self.stream.readString()

    def getMessageType(self):
        return 10102
