from VadGutTitan.Logic.Message.VersionedMessage import VersionedMessage
from VadGutTitan.Logic.DataStream.ByteStream import ByteStream
from VadGutLogic.Avatar.LogicClientAvatar import LogicClientAvatar
from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
class AvatarDataMessage(VersionedMessage):
    def  __init__(self):
        super().__init__()

    def encode(self):
        super().encode()
        LogicClientAvatar().encode(self.stream)

    
    def getMessageType(self):
        return 20201