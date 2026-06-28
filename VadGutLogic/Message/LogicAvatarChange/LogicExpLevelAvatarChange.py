from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Message.LogicAvatarChange.LogicAvatarChange import LogicAvatarChange

class LogicExpLevelAvatarChange(LogicAvatarChange):
    def __init__(self):
        super().__init__()
        self.ExpLevel = None

    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
        encoder.writeInt(self.ExpLevel)

    def getAvatarChangeType(self):
        return 7