from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Base.LogicBase import LogicBase
class LogicInventory(LogicBase):
    def __init__(self):
        self.InventoryItemCount = 0

    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
        encoder.writeInt(self.InventoryItemCount)

