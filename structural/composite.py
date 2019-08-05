from abc import ABC, abstractmethod
from random import random


class RollCall(ABC):

    @abstractmethod
    def num_member(self):
        pass

    def show_names(self):
        print(self.name)
        if hasattr(self, "parts"):
            for x in self.parts:
                x.show_names()


class Soldier(RollCall):

    def __init__(self, name="Joe"):
        self.name = name

    @property
    def num_member(self):
        return 1


class Squad(RollCall):

    def __init__(self, leader_name="Smith"):
        self.set_leader(Soldier(leader_name))
        self.parts = []

    def set_leader(self, soldier):
        self.squad_leader = soldier

    @property
    def name(self):
        return self.squad_leader.name

    @property
    def num_member(self):
        return sum([x.num_member for x in self.parts]) + self.squad_leader.num_member

    def add_member(self, name):
        self.parts.append(Soldier(name))


def main():
    squad = Squad()
    print(squad.num_member)
    squad.add_member("Prince")
    squad.add_member("Fire")
    squad.add_member("Faker")
    squad.add_member("Flash")
    squad.add_member("Mesh")
    print(squad.num_member)
    squad.show_names()


if __name__ == "__main__":
    main()