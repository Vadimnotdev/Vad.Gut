from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Base.LogicBase import LogicBase
from VadGutLogic.Calendar.LogicGameCalendar import LogicGameCalendar
class LogicAvatarTask(LogicBase):
    def __init__(self, task, diamonds):
        super().__init__()
        self.CurrentlyActiveTask = task
        self.startCalendar = LogicGameCalendar()
        self.endCalendar = LogicGameCalendar()  
        self.SpeedUpDiamondsLeft = diamonds


    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
        encoder.writeString(self.CurrentlyActiveTask)
        self.startCalendar.encode(encoder)
        self.endCalendar.encode(encoder)
        encoder.writeInt(self.SpeedUpDiamondsLeft)