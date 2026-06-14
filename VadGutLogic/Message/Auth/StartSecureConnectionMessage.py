from VadGutTitan.Logic.Message.VersionedMessage import VersionedMessage
class StartSecureConnectionMessage(VersionedMessage):
    def __init__(self):
        super().__init__()

    def decode(self):
        super().decode()
    
    def getMessageType(self):
        return 10105