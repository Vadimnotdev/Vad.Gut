from VadGutTitan.Logic.Message.VersionedMessage import VersionedMessage
class BuyMessage(VersionedMessage):
    def __init__(self):
        super().__init__()
        self.Item = None

    def decode(self):
        super().decode()
        self.Item = self.stream.readString()
    
    def getMessageType(self):
        return 10204