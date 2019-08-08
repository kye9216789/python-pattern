from abc import ABC, abstractmethod


class ControlerFactory(ABC):

    def __init__(self, creator_id):
        self.id = creator_id

    @abstractmethod
    def create_object(self, channel):
        pass



class WirelessControler(ABC):

    def __init__(self, channel):
        self.channel = channel

    @abstractmethod
    def 
