from VadGutTitan.Logic.Message.VersionedMessage import VersionedMessage
class AskForAddableFriendsMessage(VersionedMessage):
    def __init__(self):
        super().__init__()
        self.FacebookIds = 0
        self.GamecenterIds = 0

    def decode(self):
        super().decode()
        self.FacebookIds = self.stream.readInt()
        self.GamecenterIds = self.stream.readInt()
    
    def getMessageType(self):
        return 10503