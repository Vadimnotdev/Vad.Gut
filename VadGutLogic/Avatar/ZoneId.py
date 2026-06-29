from VadGutLogic.Base.LogicBase import LogicBase
from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
class ZoneId(LogicBase):
    def __init__(self, type, contanier, id):
        super().__init__()
        self.zoneType = type #1=solo, 2=multi, 3=random
        self.Container = contanier
        self.id = id

    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
        encoder.writeInt(self.zoneType)
        encoder.writeInt(self.Container)
        encoder.writeInt(0) #unknown int
        encoder.writeInt(self.id)
