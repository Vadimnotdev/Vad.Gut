from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Base.LogicBase import LogicBase
from VadGutTitan.Logic.Math.LogicLong import LogicLong
from VadGutLogic.Avatar.LogicPlayerAttributes import LogicPlayerAttributes
from VadGutLogic.Avatar.LogicInventory import LogicInventory
from VadGutLogic.Avatar.LogicPlayerStats import LogicPlayerStats
class LogicClientAvatar(LogicBase):
    def __init__(self):
        self.id = LogicLong(0, 1)
        self.ActiveMission = -1
        self.name = "Vadim"
        self.AvatarCode = ""
        self.MissionStatus = 0
        self.TutorialFlags = 0
        self.AvatarGames = 0




    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
        encoder.writeLong(self.id)
        encoder.writeInt(self.ActiveMission)
        encoder.writeString(self.name)
        encoder.writeString(self.AvatarCode)
        encoder.writeInt(self.AvatarGames)
        encoder.writeInt(self.MissionStatus)
        LogicPlayerAttributes().encode(encoder)
        LogicInventory().encode(encoder)
        LogicPlayerStats().encode(encoder)
        encoder.writeInt(self.TutorialFlags)





