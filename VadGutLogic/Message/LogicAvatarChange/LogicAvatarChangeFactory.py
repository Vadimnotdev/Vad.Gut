from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Message.LogicAvatarChange.LogicMissionAvatarChange import LogicMissionAvatarChange
from VadGutLogic.Message.LogicAvatarChange.LogicReadHandbookAvatarChange import LogicReadHandbookAvatarChange
from VadGutLogic.Message.LogicAvatarChange.LogicInventoryAvatarChange import LogicInventoryAvatarChange
from VadGutLogic.Message.LogicAvatarChange.LogicSkillTrainedAvatarChange import LogicSkillTrainedAvatarChange
from VadGutLogic.Message.LogicAvatarChange.LogicTutorialProgessAvatarChange import LogicTutorialProgessAvatarChange
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
            case 8:
                change = LogicReadHandbookAvatarChange()
                change.Item = args[0]
            case 3:
                change = LogicInventoryAvatarChange(args[0])
            case 11:
                change = LogicSkillTrainedAvatarChange()
                change.TeamUnitIndex = args[0]
                change.SkillName = args[1]
            case 16:
                change = LogicTutorialProgessAvatarChange()
                change.TutorialFlag = args[0]
            case _:
                Debugger.error(f"Unknown AvatarChangeType: {self.AvatarChangeType}")
        return change