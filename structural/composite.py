from abc import ABC, abstractmethod
from random import random


class RollCall(ABC):
    @abstractmethod
    def get_num_member(self):
        pass


class Soldier(RollCall):
    def __init__(self, name="Joe"):
        self.name = name

    def get_num_member(self):
        return 1

    def show_names(self):
        print(self.name)


class Squad(RollCall):
    def __init__(self, leader_name="Smith"):
        self.set_leader(Soldier(leader_name))
        self.parts = []

    def set_leader(self, soldier):
        self.squad_leader = soldier

    def get_num_member(self):
        return sum([x.get_num_member() for x in self.parts]) + self.squad_leader.get_num_member()

    def show_names(self):
        print(self.squad_leader.name)
        for x in self.parts:
            x.show_names()

    def add_member(self, name):
        self.parts.append(Soldier(name))


squad = Squad()
print(squad.get_num_member())
squad.add_member("Prince")
squad.add_member("Fire")
squad.add_member("Faker")
squad.add_member("Flash")
squad.add_member("Mesh")
print(squad.get_num_member())
squad.show_names()