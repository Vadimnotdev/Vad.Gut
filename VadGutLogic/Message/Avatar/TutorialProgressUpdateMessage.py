from VadGutTitan.Logic.Message.VersionedMessage import VersionedMessage
class TutorialProgressUpdateMessage(VersionedMessage):
    def __init__(self):
        super().__init__()
        self.TutorialFlag = 0

    def decode(self):
        super().decode()
        self.TutorialFlag = self.stream.readInt()
    
    def getMessageType(self):
        return 10210