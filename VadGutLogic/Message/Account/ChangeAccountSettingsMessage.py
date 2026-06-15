from VadGutTitan.Logic.Message.VersionedMessage import VersionedMessage
class ChangeAccountSettingsMessage(VersionedMessage):
    def __init__(self):
        super().__init__()
        self.SettingsMap = 0
        self.FacebookId = ""
        self.GameCenterId = ""
        self.unkStr = ""
        self.AvatarName = ""
        self.DeviceToken = None

    def decode(self):
        super().decode()
        self.SettingsMap = self.stream.readInt()
        self.FacebookId = self.stream.readString()
        self.GameCenterId = self.stream.readString()
        self.unkStr = self.stream.readString()
        self.AvatarName = self.stream.readString()
        self.DeviceToken = self.stream.readBytes(self.stream.readBytesLength())

        

    
    def getMessageType(self):
        return 10104