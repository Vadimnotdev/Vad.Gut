from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Message.LogicAvatarChange.LogicMissionAvatarChange import LogicMissionAvatarChange
from VadGutTitan.Logic.Debug.Debugger import Debugger

class LogicAvatarChangeFactory:
    def __init__(self, avatarChangeType, *args):
        self.AvatarChangeType = avatarChangeType
        self.AvatarChange = self.createChange(*args)

    def encode(self, encoder: ChecksumEncoder):
        encoder.writeInt(self.AvatarChangeType)
        self.AvatarChange.encode(encoder)

    def createChange(self, *args):
        match self.AvatarChangeType:
            case 5:
                change = LogicMissionAvatarChange()
                change.missionId = args[0]
                change.missionStatus = args[1]
                return change
            case _:
                Debugger.error(f"Unknown AvatarChangeType: {self.AvatarChangeType}")