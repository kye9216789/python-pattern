from abc import ABC, abstractmethod


class ControlerFactory(ABC):

    def __init__(self, creator_id):
        self.id = creator_id

    @abstractmethod
    def create_object(self, channel):
        pass


class AbstractControler(ABC):

    def __init__(self, channel):
        self.channel = channel

    @abstractmethod
    def control(self):
        pass


class WirelessControlerFactory(ControlerFactory):

    def __init__(self, creator_id):
        super().__init__(creator_id)

    def create_object(self, channel):
        return WirelessControler(channel)


class WireControlerFactory(ControlerFactory):

    def __init__(self, creator_id):
        super().__init__(creator_id)

    def create_object(self, channel):
        return WireControler(channel)

class WirelessControler(AbstractControler):

class WireControler(AbstractControler):