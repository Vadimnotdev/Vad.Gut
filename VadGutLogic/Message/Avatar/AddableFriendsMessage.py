from VadGutTitan.Logic.Message.VersionedMessage import VersionedMessage

class AddableFriendsMessage(VersionedMessage):
    def __init__(self):
        super().__init__()
        self.FriendRequestsCount = -1

    def encode(self):
        super().encode()
        self.stream.writeInt(self.FriendRequestsCount)

    def getMessageType(self):
        return 20107