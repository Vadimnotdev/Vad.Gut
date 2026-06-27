from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Message.LogicAvatarChange.LogicAvatarChange import LogicAvatarChange

class LogicTutorialProgessAvatarChange(LogicAvatarChange):
    def __init__(self):
        super().__init__()
        self.TutorialFlag = None

    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
        encoder.writeInt(self.TutorialFlag)


    
    def getAvatarChangeType(self):
        return 16