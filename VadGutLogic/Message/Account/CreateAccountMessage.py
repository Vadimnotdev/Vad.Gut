from VadGutTitan.Logic.Message.VersionedMessage import VersionedMessage
class CreateAccountMessage(VersionedMessage):
    def __init__(self):
        super().__init__()
        self.FacebookId = ""
        self.GameCenterId = ""

    def decode(self):
        super().decode()
        self.stream.readString()
        self.FacebookId = self.stream.readString()
        self.GameCenterId = self.stream.readString()
        self.stream.readString()
        self.stream.readString()
    
    def getMessageType(self):
        return 10103