# LogicAvatarDescriptor.py
from VadGutLogic.Base.LogicBase import LogicBase
from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder

class LogicAvatarDescriptor(LogicBase):
    def __init__(self):
        super().__init__()
        self.AvatarIdH = 0
        self.AvatarIdL = 0
        self.name = "VadimNotDev"
        self.AvatarCode = ""

    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
        encoder.writeInt(self.AvatarIdH)
        encoder.writeInt(self.AvatarIdL)
        encoder.writeString(self.name)
        encoder.writeString(self.AvatarCode)