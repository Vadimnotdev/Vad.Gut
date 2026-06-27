from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Message.LogicAvatarChange.LogicAvatarChange import LogicAvatarChange

class LogicReadHandbookAvatarChange(LogicAvatarChange):
    def __init__(self):
        super().__init__()
        self.Item = None

    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
        encoder.writeString(self.Item)

    
    def getAvatarChangeType(self):
        return 8