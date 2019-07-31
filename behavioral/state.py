from abc import ABC, abstractmethod


class WorkerState(ABC):
    def __init__(self, worker):
        self.worker = worker

    @abstractmethod
    def drink_coffee(self):
        pass

    @abstractmethod
    def do_work(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


class Fine(WorkerState):
    def __init__(self, worker):
        super(Fine, self).__init__(worker)

    def drink_coffee(self):
        self.worker.tired -= 1
        print(f"{self.worker.name} is fine! Coffee smells good!")

    def do_work(self):
        self.worker.tired += 1
        if self.worker.tired > 5:
            self.worker.change_state(Bad)
        print(f"{self.worker.name} wants some sleep")

    def sleep(self):
        print("Good night!")
        self.tired = 0


class Bad(WorkerState):
    def __init__(self, worker):
        super(Bad, self).__init__(worker)

    def drink_coffee(self):
        self.worker.tired += 1
        print(f"{self.worker.name} wants sleep")

    def do_work(self):
        self.worker.tired += 3
        print(f"{self.worker.name} wants sleep")

    def sleep(self):
        self.worker.change_state(Fine)
        print("zzz...")
        self.worker.tired = 0


class Coding(WorkerState):
    def __init__(self, worker):
        super(Coding, self).__init__(worker)
        self.worker.tired = 10

    def drink_coffee(self):
        print(f"{self.worker.name} wants some more coffee...")

    def do_work(self):
        print(f"{self.worker.name} wants some more coffee...")

    def sleep(self):
        print(f"{self.worker.name} wants some more coffee...")


class Person:
    def __init__(self, name, state):
        self.name = name
        self.state = state(self)
        self.tired = 0

    def change_state(self, state):
        if not isinstance(self.state, Coding):
            self.state = state(self)

    def drink_coffee(self):
        self.state.drink_coffee()

    def do_work(self):
        self.state.do_work()

    def sleep(self):
        self.state.sleep()


def main():

    officer = Person("Alexa", Fine)

    coder = Person("Bob", Coding)

    work_days = 10

    for _ in range(work_days):
        officer.do_work()
        officer.do_work()
        coder.do_work()
        coder.do_work()
        officer.drink_coffee()
        coder.drink_coffee()

    officer.sleep()
    coder.sleep()

    officer.drink_coffee()

    coder.change_state(Fine)
    coder.sleep()


if __name__ == "__main__":
    main()