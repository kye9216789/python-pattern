from abc import ABC, abstractmethod


class ControllerFactory(ABC):

    @abstractmethod
    def create_object(self):
        pass


class WirelessControllerFactory(ControllerFactory):

    def create_object(self, channel):
        return WirelessController(channel)



class WireControllerFactory(ControllerFactory):

    def create_object(self):
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
        print(f"This is wire controller.")

    def control(self):
        print("I can control objects that has an electric port")


if __name__ == "__main__":

    wireless_controller_factory = WirelessControllerFactory()
    wire_controller_factory = WireControllerFactory()

    print("I need a remote controller for air conditioner")
    air_conditioner_controller = wireless_controller_factory.create_object(10)

    print("I need a part of fan controller")
    fan_controller_part = wire_controller_factory.create_object()
