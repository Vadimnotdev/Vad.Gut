from VadGutTitan.Logic.Message.VersionedMessage import VersionedMessage

class BuyOkMessage(VersionedMessage):
    def __init__(self, item):
        super().__init__()
        self.Item = item

    def encode(self):
        super().encode()
        self.stream.writeString(self.Item)

    def getMessageType(self):
        return 20207