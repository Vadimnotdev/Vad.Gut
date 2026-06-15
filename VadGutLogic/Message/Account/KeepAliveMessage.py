from VadGutTitan.Logic.Message.VersionedMessage import VersionedMessage
class KeepAliveMessage(VersionedMessage):
    def __init__(self):
        super().__init__()

    def decode(self):
        super().decode()
    
    def getMessageType(self):
        return 10108