from VadGutTitan.Logic.Message.VersionedMessage import VersionedMessage
class SelectAvatarMessage(VersionedMessage):
    def __init__(self):
        super().__init__()
        self.higiId = 0
        self.lowId = 0

    def decode(self):
        super().decode()
        self.higiId = self.stream.readInt()
        self.lowId = self.stream.readInt()
    
    def getMessageType(self):
        return 10201