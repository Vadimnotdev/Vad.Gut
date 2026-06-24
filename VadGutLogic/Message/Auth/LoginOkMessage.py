from VadGutTitan.Logic.Message.VersionedMessage import VersionedMessage
from VadGutTitan.Logic.Math.LogicLong import LogicLong
from VadGutLogic.Calendar.LogicGameCalendar import LogicGameCalendar
class LoginOkMessage(VersionedMessage):
    def __init__(self):
        super().__init__()
        self.PrimaryAvatarId = LogicLong(0, 0)


    def encode(self):
        super().encode()
        self.stream.writeInt(0)
        self.stream.writeInt(0)
        self.stream.writeInt(0)#id
        self.stream.writeInt(1)#id
        self.stream.writeInt(0)
        self.stream.writeInt(0)
        self.stream.writeInt(0)
        self.stream.writeInt(0)
        self.stream.writeString("")
        LogicGameCalendar().encode(self.stream)
        self.stream.writeString("")
        self.stream.writeString("")
        self.stream.writeInt(0)



    def getMessageType(self):
        return 20104