from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Message.LogicAvatarChange.LogicAvatarChange import LogicAvatarChange

class LogicNameChangedAvatarChange(LogicAvatarChange):
    def __init__(self):
        super().__init__()
        self.Name = None
        self.AvatarCode = None

    def encode(self, encoder: ChecksumEncoder):
        encoder.writeString(self.Name)
        encoder.writeString(self.AvatarCode)

    def getAvatarChangeType(self):
        return 4