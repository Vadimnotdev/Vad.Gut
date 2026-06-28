from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Message.LogicAvatarChange.LogicAvatarChange import LogicAvatarChange
from VadGutLogic.Avatar.LogicInventory import LogicInventory
class LogicLootGainedAvatarChange(LogicAvatarChange):
    def __init__(self):
        super().__init__()
        self.InventoryItem = None
        self.LootMoney = None
        self.VictoryMoney = None
        self.ConsolationMoney = None
        self.SurvivalMoney = None

    def encode(self, encoder: ChecksumEncoder):
        encoder.writeString(self.InventoryItem)
        encoder.writeInt(self.LootMoney)
        encoder.writeInt(self.VictoryMoney)
        encoder.writeInt(self.ConsolationMoney)
        encoder.writeInt(self.SurvivalMoney)
        LogicInventory().encode(encoder)

    def getAvatarChangeType(self):
        return 14