from VadGutTitan.Logic.Message.VersionedMessage import VersionedMessage

class FriendListMessage(VersionedMessage):
    def __init__(self):
        super().__init__()
        self.FriendsCount = -1

    def encode(self):
        super().encode()
        self.stream.writeInt(self.FriendsCount)

    def getMessageType(self):
        return 20105