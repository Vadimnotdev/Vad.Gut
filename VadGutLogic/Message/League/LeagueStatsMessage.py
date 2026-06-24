from VadGutTitan.Logic.Message.VersionedMessage import VersionedMessage
from VadGutLogic.Message.League.LogicLeagueEntry import LogicLeagueEntry
from VadGutLogic.Calendar.LogicGameCalendar import LogicGameCalendar
class LeagueStatsMessage(VersionedMessage):
    def __init__(self):
        super().__init__()
        self.Division = 1
        self.League = 0
        self.PlayersCount = 1

    def encode(self):
        super().encode()
        self.stream.writeInt(self.Division)
        self.stream.writeInt(self.League)
        self.stream.writeInt(self.PlayersCount)
        LogicLeagueEntry().encode(self.stream)
        LogicGameCalendar().encode(self.stream)


    def getMessageType(self):
        return 20601