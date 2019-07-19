from abc import ABC, abstractmethod
from random import random


class Command(ABC):
    def __init__(self, receiver, input_str):
        self.receiver = receiver
        self.input_str = input_str

    @abstractmethod
    def execute(self):
        pass


class PrintOnce(Command):
    def __init__(self, receiver, input_str):
        super(PrintOnce, self).__init__(receiver, input_str)
        self.num_iter = 1

    def execute(self):
        self.receiver.print_header()
        self.receiver.print_string(self.input_str, self.num_iter)
        self.receiver.print_header()


class PrintTwice(Command):
    def __init__(self, receiver, input_str):
        super(PrintTwice, self).__init__(receiver, input_str)
        self.num_iter = 2

    def execute(self):
        self.receiver.print_header()
        self.receiver.print_header()
        self.receiver.print_string(self.input_str, self.num_iter)
        self.receiver.print_header()
        self.receiver.print_header()


class Receiver:
    def print_header(self):
        print("================")

    def print_string(self, input_str, num_iter):
        for _ in range(num_iter):
            print(input_str)


class Sender:
    def __init__(self):
        self.command = []
    def set_command(self, command):
        self.command.append(command)

    def execute_command(self, idx):
        self.command[idx].execute()


class Client:
    def __init__(self, input_str):
        receiver = Receiver()
        self.printer = Sender()
        self.printer.set_command(PrintOnce(receiver, input_str))
        self.printer.set_command(PrintTwice(receiver, input_str))


if __name__ == "__main__":
    client = Client("Design Pattern!!")

    rand = int(random() * 10) % 2
    client.printer.execute_command(rand)
