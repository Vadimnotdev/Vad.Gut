from VadGutTitan.Logic.Message.VersionedMessage import VersionedMessage
class TrainMessage(VersionedMessage):
    def __init__(self):
        super().__init__()
        self.TeamUnitIndex = None
        self.SkillName = None

    def decode(self):
        super().decode()
        self.TeamUnitIndex = self.stream.readInt()
        self.SkillName = self.stream.readString()

    
    def getMessageType(self):
        return 10203