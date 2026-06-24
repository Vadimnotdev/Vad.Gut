from VadGutTitan.Logic.Message.VersionedMessage import VersionedMessage
from VadGutLogic.Message.LogicAvatarChange.LogicAvatarChangeFactory import LogicAvatarChangeFactory

class LogicAvatarChangeMessage(VersionedMessage):
    def __init__(self,  AvatarChangeList, *args):
        super().__init__()
        self.AvatarChangeList = AvatarChangeList
        self.args = args

    def encode(self):
        super().encode()
        self.stream.writeInt(len(self.AvatarChangeList))
        for (changeType, *args) in self.AvatarChangeList:
            LogicAvatarChangeFactory(changeType, *args).encode(self.stream)

    def getMessageType(self):
        return 20209