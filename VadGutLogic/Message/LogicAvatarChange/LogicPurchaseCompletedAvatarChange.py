from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Message.LogicAvatarChange.LogicAvatarChange import LogicAvatarChange
from VadGutLogic.Message.LogicAvatarChange.LogicDiamondsAvatarChange import LogicDiamondsAvatarChange

class LogicPurchaseCompletedAvatarChange(LogicAvatarChange):
    def __init__(self):
        super().__init__()
        self.PurchaseId = None
        self.price = None

    def encode(self, encoder: ChecksumEncoder):
        LogicDiamondsAvatarChange(self.price).encode(encoder)
        encoder.writeInt(self.PurchaseId)

    def getAvatarChangeType(self):
        return 12