from VadGutLogic.Base.LogicBase import LogicBase
from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Avatar.ZoneId import ZoneId
from VadGutLogic.Calendar.LogicGameCalendar import LogicGameCalendar
class LogicAvatarGame(LogicBase):
    def __init__(self, type, cont, id, hId, lId, game, turn, level):
        super().__init__()
        self.zoneType = type
        self.contanier = cont
        self.id = id
        self.CreatorAvatarIdHigherInt = hId
        self.CreatorAvatarIdLowerInt = lId
        self.GameState = game
        self.TurnState = turn
        self.LevelId = level

    
    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
        ZoneId(self.zoneType, self.contanier, self.id).encode(encoder)
        encoder.writeInt(self.CreatorAvatarIdHigherInt)
        encoder.writeInt(self.CreatorAvatarIdLowerInt)
        encoder.writeInt(self.GameState)
        encoder.writeInt(self.TurnState)
        LogicGameCalendar().encode(encoder)
        encoder.writeString(self.LevelId)
