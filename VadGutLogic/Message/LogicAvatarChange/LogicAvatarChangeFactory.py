from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Message.LogicAvatarChange.LogicMissionAvatarChange import LogicMissionAvatarChange
from VadGutLogic.Message.LogicAvatarChange.LogicReadHandbookAvatarChange import LogicReadHandbookAvatarChange
from VadGutLogic.Message.LogicAvatarChange.LogicInventoryAvatarChange import LogicInventoryAvatarChange
from VadGutLogic.Message.LogicAvatarChange.LogicSkillTrainedAvatarChange import LogicSkillTrainedAvatarChange
from VadGutLogic.Message.LogicAvatarChange.LogicTutorialProgessAvatarChange import LogicTutorialProgessAvatarChange
from VadGutLogic.Message.LogicAvatarChange.LogicDiamondsGainedAvatarChange import LogicDiamondsGainedAvatarChange
from VadGutLogic.Message.LogicAvatarChange.LogicMoneyAvatarChange import LogicMoneyAvatarChange
from  VadGutLogic.Message.LogicAvatarChange.LogicExpPointsAvatarChange import LogicExpPointsAvatarChange
from VadGutLogic.Message.LogicAvatarChange.LogicExpLevelAvatarChange import LogicExpLevelAvatarChange
from VadGutLogic.Message.LogicAvatarChange.LogicPurchaseCompletedAvatarChange import LogicPurchaseCompletedAvatarChange
from VadGutLogic.Message.LogicAvatarChange.LogicStatsAvatarChange import LogicStatsAvatarChange
from VadGutLogic.Message.LogicAvatarChange.LogicLeagueMMRAvatarChange import LogicLeagueMMRAvatarChange
from VadGutLogic.Message.LogicAvatarChange.LogicNameChangedAvatarChange import LogicNameChangedAvatarChange
from VadGutLogic.Message.LogicAvatarChange.LogicLootGainedAvatarChange import LogicLootGainedAvatarChange
from VadGutLogic.Message.LogicAvatarChange.LogicSetActiveTaskAvatarChange import LogicSetActiveTaskAvatarChange
from VadGutLogic.Message.LogicAvatarChange.LogicClearActiveTaskAvatarChange import LogicClearActiveTaskAvatarChange
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
            case 1:
                change = LogicDiamondsGainedAvatarChange()
                change.count = args[0]
            case 2:
                change = LogicMoneyAvatarChange()
                change.count = args[0]
            case 3:
                change = LogicInventoryAvatarChange(args[0])
            case 4:
                change = LogicNameChangedAvatarChange()
                change.Name = args[0]
                change.AvatarCode = args[1]
            case 5:
                change = LogicMissionAvatarChange()
                change.missionId = args[0]
                change.missionStatus = args[1]
            case 6:
                change = LogicExpPointsAvatarChange()
                change.ExpPointsArray = args[0]
            case 7:
                change = LogicExpLevelAvatarChange()
                change.ExpLevel = args[0]
            case 8:
                change = LogicReadHandbookAvatarChange()
                change.Item = args[0]
            case 9:
                change = LogicSetActiveTaskAvatarChange()
                change.TaskType = args[0]
                change.args = args[1]
            case 10:
                change = LogicClearActiveTaskAvatarChange()
            case 11:
                change = LogicSkillTrainedAvatarChange()
                change.TeamUnitIndex = args[0]
                change.SkillName = args[1]
            case 12:
                change = LogicPurchaseCompletedAvatarChange()
                change.price = args[0]
                change.PurchaseId = args[1]
            case 14:
                change = LogicLootGainedAvatarChange()
                change.InventoryItem = args[0]
                change.LootMoney = args[1]
                change.VictoryMoney = args[2]
                change.ConsolationMoney = args[3]
                change.SurvivalMoney = args[4]
            case 15:
                change = LogicStatsAvatarChange()
                change.Score = args[0]
                change.MatchCount = args[1]
                change.WinCount = args[2]
                change.KillCount = args[3]
                change.isInLeague = args[4]
                change.Division = args[5]
                change.League = args[6]
            case 16:
                change = LogicTutorialProgessAvatarChange()
                change.TutorialFlag = args[0]
            case 18:
                change = LogicLeagueMMRAvatarChange()
                change.LeagueMmr = args[0]
                change.LeagueMmrKFactor = args[1]
            case _:
                Debugger.error(f"Unknown AvatarChangeType: {self.AvatarChangeType}")
        return change