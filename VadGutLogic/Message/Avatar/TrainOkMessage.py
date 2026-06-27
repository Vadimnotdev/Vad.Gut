from VadGutTitan.Logic.Message.VersionedMessage import VersionedMessage

class TrainOkMessage(VersionedMessage):
    def __init__(self, index, skill):
        super().__init__()
        self.TeamUnitIndex = index
        self.SkillName = skill

    def encode(self):
        super().encode()
        self.stream.writeInt(self.TeamUnitIndex)
        self.stream.writeString(self.SkillName)


    def getMessageType(self):
        return 20205