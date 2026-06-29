from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Base.LogicBase import LogicBase
from VadGutTitan.Logic.Math.LogicLong import LogicLong
from VadGutLogic.Avatar.LogicPlayerAttributes import LogicPlayerAttributes
from VadGutLogic.Avatar.LogicInventory import LogicInventory
from VadGutLogic.Avatar.LogicPlayerStats import LogicPlayerStats
from VadGutLogic.Avatar.LogicAvatarGame import LogicAvatarGame
class LogicClientAvatar(LogicBase):
    def __init__(self, ): #type, cont, id, hId, lId, game, turn, level, avatarGames, missionStatus
        super().__init__()
        self.id = LogicLong(0, 1)
        self.ActiveMission = -1
        self.name = "Vadim"
        self.AvatarCode = ""
        self.AvatarGames = 0

        # self.zoneType = type
        # self.contanier = cont
        # self.id = id
        # self.CreatorAvatarIdHigherInt = hId
        # self.CreatorAvatarIdLowerInt = lId
        # self.GameState = game
        # self.TurnState = turn
        # self.LevelId = level

        self.MissionStatus = []
            # (0x1C << 16) | 2000,
            # (0x1C << 16) | 2001,
            # (0x1C << 16) | 2002,
            # (0x12 << 16) | 2003,
         #missionStatus
        self.TutorialFlags = 999

    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
        encoder.writeLong(self.id)
        encoder.writeInt(self.ActiveMission)
        encoder.writeString(self.name)
        encoder.writeString(self.AvatarCode)
        encoder.writeInt(self.AvatarGames)
        for i in range(self.AvatarGames):
            LogicAvatarGame(self.zoneType, self.contanier, self.id, self.CreatorAvatarIdHigherInt, self.CreatorAvatarIdLowerInt, self.GameState, self.TurnState, self.LevelId).encode(encoder)
        encoder.writeInt(len(self.MissionStatus)) 
        for status in self.MissionStatus:
            encoder.writeInt(status)
        LogicPlayerAttributes().encode(encoder)
        LogicInventory().encode(encoder)
        LogicPlayerStats().encode(encoder)
        encoder.writeInt(self.TutorialFlags)
