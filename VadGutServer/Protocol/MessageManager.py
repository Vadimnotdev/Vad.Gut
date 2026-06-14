from VadGutTitan.Logic.Debug.Debugger import Debugger
from VadGutLogic.Message.Auth.SecureConnectionOkMessage import SecureConnectionOkMessage
from VadGutTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from VadGutLogic.Message.Account.CreateAccountOkMessage import CreateAccountOkMessage
from VadGutLogic.Message.Auth.LoginOkMessage import LoginOkMessage
from VadGutLogic.Message.Account.AvatarDataMessage import AvatarDataMessage
from VadGutLogic.Avatar.AskForFriendListMessage import AskForFriendListMessage
from VadGutLogic.Avatar.FriendListMessage import FriendListMessage
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
            case _:
                Debugger.warning("Unknown message type: " + str(messageType))

    def __str__(self) -> str:
        return f"{self.highInteger}-{self.lowInteger}"
    
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