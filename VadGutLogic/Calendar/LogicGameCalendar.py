from VadGutLogic.Base.LogicBase import LogicBase
from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder

class LogicGameCalendar(LogicBase):
    def __init__(self):
        super().__init__()


    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
        encoder.writeInt(0)
        encoder.writeByte(0)
        encoder.writeByte(0)
        encoder.writeByte(0)
        encoder.writeByte(0)
        encoder.writeByte(0)
        encoder.writeInt(0)
        encoder.writeInt(0)
