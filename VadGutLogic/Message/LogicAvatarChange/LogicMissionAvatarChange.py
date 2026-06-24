from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Message.LogicAvatarChange.LogicAvatarChange import LogicAvatarChange

class LogicMissionAvatarChange(LogicAvatarChange):
    def __init__(self):
        super().__init__()
        self.missionId = 0
        self.missionStatus = 0
        self.resetFlag = False

    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
        encoder.writeInt(self.missionId)
        encoder.writeInt(self.missionStatus)
        encoder.writeBoolean(self.resetFlag)
    
    def getAvatarChangeType(self):
        return 5