from VadGutLogic.Base.LogicBase import LogicBase
from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder

class LogicInventory(LogicBase):
    def __init__(self):
        super().__init__()
        self.categoryCount = None
        self.InventoryItemCount = None
        

    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
