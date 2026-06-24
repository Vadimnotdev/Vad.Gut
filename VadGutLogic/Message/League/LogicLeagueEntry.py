from VadGutLogic.Base.LogicBase import LogicBase
from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Avatar.LogicAvatarDescriptor import LogicAvatarDescriptor
class LogicLeagueEntry(LogicBase):
    def __init__(self):
        super().__init__()
        self.Points = 1
        self.Wins = 2


    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
        encoder.writeInt(self.Points)
        encoder.writeInt(self.Wins)
        LogicAvatarDescriptor().encode(encoder)

