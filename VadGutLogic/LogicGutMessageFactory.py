from VadGutLogic.Message.Auth.StartSecureConnectionMessage import StartSecureConnectionMessage
from VadGutLogic.Message.Account.CreateAccountMessage import CreateAccountMessage
from VadGutLogic.Message.Auth.LoginUsingSessionMessage import LoginUsingSessionMessage
from VadGutLogic.Message.Account.SelectAvatarMessage import SelectAvatarMessage
from VadGutLogic.Message.Account.CreateAvatarMessage import CreateAvatarMessage
from VadGutLogic.Avatar.AskForFriendListMessage import AskForFriendListMessage


class LogicGutMessageFactory:
    messages = {
        10105: StartSecureConnectionMessage,
        10103: CreateAccountMessage,
        10102: LoginUsingSessionMessage,
        10201: SelectAvatarMessage,
        10200: CreateAvatarMessage,
        10504: AskForFriendListMessage,

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