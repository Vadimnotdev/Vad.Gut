from VadGutTitan.Logic.Message.VersionedMessage import VersionedMessage
class MissionStatusMessage(VersionedMessage):
    def __init__(self):
        super().__init__()
        self.MissionId = 0
        self.MissionStatus = 0


    def decode(self):
        super().decode()
        self.MissionId = self.stream.readInt()
        self.MissionStatus = self.stream.readByte()
    
    def getMessageType(self):
        return 10209