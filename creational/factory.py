from abc import ABC, abstractmethod


class ControllerFactory(ABC):

    def __init__(self, creator_id):
        self.id = creator_id

    def create_object(self, channel=None):
        if channel is not None:
            return WirelessController(channel)
        else:
            return WireController()


class AbstractController(ABC):

    @abstractmethod
    def control(self):
        pass


class WirelessController(AbstractController):

    def __init__(self, channel):
        self.channel = channel
        print(f"This is wireless controller. Channel number is {self.channel}")

    def control(self):
        print("I can control any objects")


class WireController(AbstractController):

    def __init__(self):
        print(f"This is wire controller. Channel number is not nedded")

    def control(self):
        print("I can control objects that has an outlet")


if __name__ == "__main__":
    print("I need wireless controller")
    controller_a = ControllerFactory('abc').create_object(10)

    print("I need wire controller")
    controller_b = ControllerFactory('efg').create_object()
