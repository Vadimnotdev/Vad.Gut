from VadGutLogic.Base.LogicBase import LogicBase
from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
class LogicInventory(LogicBase):
    def __init__(self):
        super().__init__()
        self.categoryCount = 0
        self.items = [[] for _ in range(self.categoryCount)]

    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
        encoder.writeInt(self.categoryCount)
        for category in self.items:
            encoder.writeInt(len(category))
            for itemName, itemAmount in category:
                encoder.writeString(itemName)
                encoder.writeInt(itemAmount)