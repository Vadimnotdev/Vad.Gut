from VadGutTitan.Logic.Message.VersionedMessage import VersionedMessage
from VadGutLogic.Message.LogicAvatarChange.LogicAvatarChangeFactory import LogicAvatarChangeFactory

class LogicAvatarChangeMessage(VersionedMessage):
    def __init__(self, avatarChangeType, *args):
        super().__init__()
        self.AvatarChangeList = 1
        self.avatarChangeType = avatarChangeType
        self.args = args

    def encode(self):
        super().encode()
        self.stream.writeInt(self.AvatarChangeList)
        LogicAvatarChangeFactory(self.avatarChangeType, *self.args).encode(self.stream)

    def getMessageType(self):
        return 20209