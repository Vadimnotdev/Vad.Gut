from VadGutTitan.Logic.Message.VersionedMessage import VersionedMessage
class ReadHandbookMessage(VersionedMessage):
    def __init__(self):
        super().__init__()
        self.BookName = None

    def decode(self):
        super().decode()
        self.BookName = self.stream.readString()
    
    def getMessageType(self):
        return 10202