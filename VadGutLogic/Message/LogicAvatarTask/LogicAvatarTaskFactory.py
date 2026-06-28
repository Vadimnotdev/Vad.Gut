from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Message.LogicAvatarTask.LogicReadingHandbookTask import LogicReadingHandbookTask
from VadGutLogic.Message.LogicAvatarTask.LogicTrainingSkillTask import LogicTrainingSkillTask
from VadGutTitan.Logic.Debug.Debugger import Debugger

class LogicAvatarTaskFactory:
    def __init__(self, type, *args):
        self.TaskType = type
        self.AvatarTask = self.createTask(*args)

    def encode(self, encoder: ChecksumEncoder):
        encoder.writeInt(self.TaskType)
        self.AvatarTask.encode(encoder)
    
    def createTask(self, *args):
        match self.TaskType:
            case 1:
                task = LogicReadingHandbookTask()
                task.CurrentlyActiveTask = args[0]
                task.SpeedUpDiamondsLeft = args[1]
            case 2:
                task = LogicTrainingSkillTask()
                task.CurrentlyActiveTask = args[0]
                task.SpeedUpDiamondsLeft = args[1]
                task.UnitIndex = args[2]
            case _:
                Debugger.error(f"Unknown AvatarTask: {self.AvatarTask}")
        return task