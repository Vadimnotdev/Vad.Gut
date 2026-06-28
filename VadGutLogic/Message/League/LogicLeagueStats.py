from VadGutLogic.Base.LogicBase import LogicBase
from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
class LogicLeagueStats(LogicBase):
    def __init__(self, division, league):
        super().__init__()
        self.Division = division
        self.League = league


    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
        encoder.writeInt(self.Division)
        encoder.writeInt(self.League)