from VadGutTitan.Logic.Message.VersionedMessage import VersionedMessage

class ReadHandbookOkMessage(VersionedMessage):
    def __init__(self, book):
        super().__init__()
        self.BookName = book

    def encode(self):
        super().encode()
        self.stream.writeString(self.BookName)

    def getMessageType(self):
        return 20203