from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Message.LogicAvatarChange.LogicAvatarChange import LogicAvatarChange

class LogicMoneyAvatarChange(LogicAvatarChange):
    def __init__(self):
        super().__init__()
        self.count = None

    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
        encoder.writeInt(self.count)


    def getAvatarChangeType(self):
        return 2