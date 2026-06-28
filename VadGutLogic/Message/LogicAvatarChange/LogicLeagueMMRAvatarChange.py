from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Message.LogicAvatarChange.LogicAvatarChange import LogicAvatarChange

class LogicLeagueMMRAvatarChange(LogicAvatarChange):
    def __init__(self):
        super().__init__()
        self.LeagueMmr = None
        self.LeagueMmrKFactor = None

    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
        encoder.writeInt(self.LeagueMmr)
        encoder.writeInt(self.LeagueMmrKFactor)
        encoder.writeInt(0)
        encoder.writeInt(0)
        encoder.writeInt(0)

    def getAvatarChangeType(self):
        return 18