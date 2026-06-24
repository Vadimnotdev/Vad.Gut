from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Base.LogicBase import LogicBase
class LogicAvatarChange(LogicBase):
    def __init__(self):
        super().__init__()
    
    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)