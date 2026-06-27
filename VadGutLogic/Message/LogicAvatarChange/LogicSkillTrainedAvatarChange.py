from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Message.LogicAvatarChange.LogicAvatarChange import LogicAvatarChange

class LogicSkillTrainedAvatarChange(LogicAvatarChange):
    def __init__(self):
        super().__init__()
        self.TeamUnitIndex = None
        self.SkillName = None

    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
        encoder.writeInt(self.TeamUnitIndex)
        encoder.writeString(self.SkillName)

    
    def getAvatarChangeType(self):
        return 11