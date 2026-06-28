from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Message.LogicAvatarChange.LogicAvatarChange import LogicAvatarChange
from VadGutLogic.Message.League.LogicLeagueStats import LogicLeagueStats
class LogicStatsAvatarChange(LogicAvatarChange):
    def __init__(self):
        super().__init__()
        self.Score = None
        self.MatchCount = None
        self.WinCount = None
        self.KillCount = None
        self.isInLeague = None
        self.Division = None
        self.League = None

    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
        encoder.writeInt(self.Score)
        encoder.writeInt(self.MatchCount)
        encoder.writeInt(self.WinCount)
        encoder.writeInt(self.KillCount)
        encoder.writeInt(self.isInLeague)
        if self.isInLeague == True:
            LogicLeagueStats(self.Division, self.League).encode(encoder)

    def getAvatarChangeType(self):
        return 15