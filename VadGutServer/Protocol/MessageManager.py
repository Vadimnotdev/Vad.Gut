from VadGutTitan.Logic.Debug.Debugger import Debugger
from VadGutLogic.Message.Auth.SecureConnectionOkMessage import SecureConnectionOkMessage
from VadGutTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from VadGutLogic.Message.Account.CreateAccountOkMessage import CreateAccountOkMessage
from VadGutLogic.Message.Auth.LoginOkMessage import LoginOkMessage
from VadGutLogic.Message.Account.AvatarDataMessage import AvatarDataMessage
from VadGutLogic.Message.Avatar.FriendListMessage import FriendListMessage
from VadGutLogic.Message.Avatar.AddableFriendsMessage import AddableFriendsMessage
from VadGutLogic.Message.Avatar.BuyOkMessage import BuyOkMessage
from VadGutLogic.Message.Avatar.BuyMessage import BuyMessage
from VadGutLogic.Message.LogicAvatarChange.LogicAvatarChangeMessage import LogicAvatarChangeMessage
from VadGutLogic.Message.Avatar.MissionStatusMessage import MissionStatusMessage
from VadGutLogic.Message.League.LeagueStatsMessage import LeagueStatsMessage
from VadGutServer.Protocol.Messaging import Messaging

class MessageManager:
    def __init__(self, messaging: Messaging) -> None:
        self.messaging = messaging

    def receiveMessage(self, message: PiranhaMessage):
        messageType = message.getMessageType()
        match messageType:
            case 10105:
                self.onStartSecureConnectionMessage(message)  
            case 10103:
                self.onCreateAccountMessage(message)
            case 10102:
                self.onLoginUsingSessionMessage(message)
            case 10201:
                self.onSelectAvatarMessage(message)
            case 10504:
                self.onAskForFriendListMessage(message)
            case 10503:
                self.onAskForAddableFriendsMessage(message)
            case 10204:
                self.onBuyMessage(message)
            case 10209:
                self.onLogicMissionAvatarChange(message)
            case 10601:
                self.onAskForLeagueStatsMessage(message)
            case _:
                if messageType != 10108:
                    Debugger.warning("Unknown message type: " + str(messageType))
    
    def onStartSecureConnectionMessage(self, message):
        self.messaging.sendMessage(SecureConnectionOkMessage())
    
    def onCreateAccountMessage(self, message):
        self.messaging.sendMessage(CreateAccountOkMessage())
    
    def onLoginUsingSessionMessage(self, message):
        self.messaging.sendMessage(LoginOkMessage())
    
    def onSelectAvatarMessage(self, message):
        self.messaging.sendMessage(AvatarDataMessage())
    
    def onAskForFriendListMessage(self, message):
        self.messaging.sendMessage(FriendListMessage())
    
    def onAskForAddableFriendsMessage(self, message):
        self.messaging.sendMessage(AddableFriendsMessage())
    
    def onBuyMessage(self, message):
        buyMessage = BuyMessage()
        self.messaging.sendMessage(BuyOkMessage(buyMessage.Item))
    
    def onLogicMissionAvatarChange(self, message: MissionStatusMessage):
        if message.MissionStatus == 12: # 1 = start, 2 = continue 12=win  3 = lose  4 = surrender   (5, message.MissionId, 28), (5, message.MissionId + 1, 1)
            self.messaging.sendMessage(LogicAvatarChangeMessage([(5, message.MissionId + 1, 18)]))#28 = CurrentFinishedReplay  18 = NextUnlockedContinue 16 = MissionSkip

    def onAskForLeagueStatsMessage(self, message):
        self.messaging.sendMessage(LeagueStatsMessage())