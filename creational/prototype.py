from abc import ABC, abstractmethod


class AbstractPrototypeFlowerBouquet(ABC):

    def __init__(self):
        self.flowers = {}
        self.basket = None
        self.price = 0

    @abstractmethod
    def clone(self):



class FlowerShop:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        for flower in item['flowers'].keys():

