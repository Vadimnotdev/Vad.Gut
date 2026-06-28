from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Message.LogicAvatarChange.LogicAvatarChange import LogicAvatarChange

class LogicExpPointsAvatarChange(LogicAvatarChange):
    def __init__(self):
        super().__init__()
        self.ExpPointsArray = None

    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
        encoder.writeInt(len(self.ExpPointsArray))
        for i in self.ExpPointsArray:
            encoder.writeInt(i)


    def getAvatarChangeType(self):
        return 6