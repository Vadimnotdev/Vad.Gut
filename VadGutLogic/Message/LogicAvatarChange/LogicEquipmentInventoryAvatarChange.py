from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Message.LogicAvatarChange.LogicAvatarChange import LogicAvatarChange

class LogicEquipmentInventoryAvatarChange(LogicAvatarChange):
    def __init__(self):
        super().__init__()
        self.isEquipped = None

    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)

    def getAvatarChangeType(self):
        return 17