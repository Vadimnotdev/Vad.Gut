from VadGutLogic.Message.Auth.StartSecureConnectionMessage import StartSecureConnectionMessage
from VadGutLogic.Message.Account.CreateAccountMessage import CreateAccountMessage
from VadGutLogic.Message.Auth.LoginUsingSessionMessage import LoginUsingSessionMessage
from VadGutLogic.Message.Account.SelectAvatarMessage import SelectAvatarMessage
from VadGutLogic.Message.Account.CreateAvatarMessage import CreateAvatarMessage
from VadGutLogic.Message.Avatar.AskForFriendListMessage import AskForFriendListMessage
from VadGutLogic.Message.Avatar.AskForAddableFriendsMessage import AskForAddableFriendsMessage
from VadGutLogic.Message.Avatar.TutorialProgressUpdateMessage import TutorialProgressUpdateMessage
from VadGutLogic.Message.Avatar.MissionStatusMessage import MissionStatusMessage
from VadGutLogic.Message.Account.ChangeAccountSettingsMessage import ChangeAccountSettingsMessage
from VadGutLogic.Message.Account.KeepAliveMessage import KeepAliveMessage
from VadGutLogic.Message.Avatar.BuyMessage import BuyMessage
from VadGutLogic.Message.League.AskForLeagueStatsMessage import AskForLeagueStatsMessage
from VadGutLogic.Message.Avatar.ReadHandbookMessage import ReadHandbookMessage
from VadGutLogic.Message.Avatar.TrainMessage import TrainMessage


class LogicGutMessageFactory:
    messages = {
        10105: StartSecureConnectionMessage,
        10103: CreateAccountMessage,
        10102: LoginUsingSessionMessage,
        10201: SelectAvatarMessage,
        10200: CreateAvatarMessage,
        10504: AskForFriendListMessage,
        10503: AskForAddableFriendsMessage,
        10209: MissionStatusMessage,
        10210: TutorialProgressUpdateMessage,
        10104: ChangeAccountSettingsMessage,
        10108: KeepAliveMessage,
        10204: BuyMessage,
        10601: AskForLeagueStatsMessage,
        10202: ReadHandbookMessage,
        10203: TrainMessage,
        }
    def createMessageByType(messageType):
        messages = LogicGutMessageFactory.messages
        if (messageType in LogicGutMessageFactory.messages.keys()):
            if (type(messages[messageType]) is None):
                pass
            else:
                return messages[messageType]()
        else:
            return None