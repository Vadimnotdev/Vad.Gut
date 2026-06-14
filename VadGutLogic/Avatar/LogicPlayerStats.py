from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Base.LogicBase import LogicBase
class LogicPlayerStats(LogicBase):
    def __init__(self):
        self.Score = 0
        self.MatchCount = 0
        self.WinCount = 0
        self.KillCount = 0

    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
        encoder.writeInt(self.Score)
        encoder.writeInt(self.MatchCount)
        encoder.writeInt(self.WinCount)
        encoder.writeInt(self.KillCount)
