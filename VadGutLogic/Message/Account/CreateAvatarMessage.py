from VadGutTitan.Logic.Message.VersionedMessage import VersionedMessage
class CreateAvatarMessage(VersionedMessage):
    def __init__(self):
        super().__init__()
        self.Name = ""

    def decode(self):
        super().decode()
        self.Name = self.stream.readString()
    
    def getMessageType(self):
        return 10200