from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Message.LogicAvatarTask.LogicAvatarTask import LogicAvatarTask

class LogicTrainingSkillTask(LogicAvatarTask):
    def __init__(self):
        super().__init__()
        self.CurrentlyActiveTask = None
        self.SpeedUpDiamondsLeft = None
        self.UnitIndex = None

    def encode(self, encoder: ChecksumEncoder):
        LogicAvatarTask(self.CurrentlyActiveTask, self.SpeedUpDiamondsLeft).encode(encoder)
        encoder.writeInt(self.UnitIndex)
    
    def getTaskType():
        return 2