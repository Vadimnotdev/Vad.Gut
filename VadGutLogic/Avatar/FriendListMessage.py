from VadGutTitan.Logic.Message.VersionedMessage import VersionedMessage

class FriendListMessage(VersionedMessage):
    def __init__(self):
        super().__init__()


    def encode(self):
        super().encode()
        self.stream.writeInt(-1)

    def getMessageType(self):
        return 20105