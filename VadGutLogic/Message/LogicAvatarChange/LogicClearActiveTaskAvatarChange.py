from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Message.LogicAvatarChange.LogicAvatarChange import LogicAvatarChange

class LogicClearActiveTaskAvatarChange(LogicAvatarChange):
    def __init__(self):
        super().__init__()

    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)

    def getAvatarChangeType(self):
        return 10