from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Base.LogicBase import LogicBase
from VadGutLogic.Avatar.LogicTeamUnit import LogicTeamUnit
class LogicPlayerAttributes(LogicBase):
    def __init__(self):
        self.expLevel = 1
        self.expPoints = 0
        self.money = 99999
        self.diamonds = 99999
        self.leagueMmr = 0
        self.leagueMmrKFactor = 0
        self.teamName = "Vadim"
        
        self.teamUnits = []
        for i in range(5):
            self.teamUnits.append(LogicTeamUnit(index=i))
            
        self.readHandbooks = []

    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
        
        encoder.writeInt(self.expLevel)
        encoder.writeInt(self.expPoints)
        encoder.writeInt(self.money)
        encoder.writeInt(self.diamonds)
        encoder.writeInt(self.leagueMmr)
        encoder.writeInt(self.leagueMmrKFactor)
        encoder.writeString(self.teamName)

        encoder.writeInt(len(self.teamUnits))
        for unit in self.teamUnits:
            unit.encode(encoder)

        encoder.writeInt(len(self.readHandbooks))
        for book in self.readHandbooks:
            encoder.writeString(book)
            
        encoder.writeInt(-1)
        encoder.writeInt(0)