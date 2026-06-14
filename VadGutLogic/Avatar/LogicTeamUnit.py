from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Base.LogicBase import LogicBase
class LogicTeamUnit(LogicBase):
    DEFAULT_SKILLS = {
        0: "sk_magnum0",
        1: "sk_grenade0",
        2: "sk_magnum0",
        3: "sk_magnum0",
        4: "sk_grenade0",
    }

    def __init__(self, index: int):
        self.name = f"un_default{index}"
        self.skills = [self.DEFAULT_SKILLS[index]] if index in self.DEFAULT_SKILLS else []

    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder) 

        encoder.writeInt(0)
        encoder.writeString(self.name)
        
        encoder.writeInt(len(self.skills))

        for skill in self.skills:
            encoder.writeString(skill)
        encoder.writeString(None)
            