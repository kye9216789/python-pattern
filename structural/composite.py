from abc import ABC, abstractmethod
from random import random


class RollCall(ABC):
    @abstractmethod
    def get_num_member(self):
        pass


class Soldier(RollCall):
    def get_num_member(self):
        return 1


class Squad(RollCall):
    def __init__(self):
        self.squad_leader = Soldier()
        self.parts = []

    def get_num_member(self):
        return sum([x.get_num_member() for x in self.parts]) + self.squad_leader.get_num_member()

    def add_member(self):
        self.parts.append(Soldier())


squad = Squad()
print(squad.get_num_member())
squad.add_member()
squad.add_member()
squad.add_member()
squad.add_member()
squad.add_member()
print(squad.get_num_member())
