from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Message.LogicAvatarTask.LogicAvatarTask import LogicAvatarTask

class LogicReadingHandbookTask(LogicAvatarTask):
    def __init__(self):
        super().__init__()
        self.CurrentlyActiveTask = None
        self.SpeedUpDiamondsLeft = None

    def encode(self, encoder: ChecksumEncoder):
        LogicAvatarTask(self.CurrentlyActiveTask, self.SpeedUpDiamondsLeft).encode(encoder)
    
    def getTaskType():
        return 1