from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Message.LogicAvatarChange.LogicAvatarChange import LogicAvatarChange
from VadGutLogic.Message.LogicAvatarTask import LogicAvatarTaskFactory

class LogicSetActiveTaskAvatarChange(LogicAvatarChange):
    def __init__(self, type, *args):
        super().__init__()
        self.TaskType = type
        self.args = args

    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
        LogicAvatarTaskFactory(self.TaskType, *self.args).encode(encoder)

    def getAvatarChangeType(self):
        return 9