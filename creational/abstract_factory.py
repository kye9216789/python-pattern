from abc import ABC, abstractmethod


class AbstractPizzaStore(ABC):

    @abstractmethod
    def make_simple_pizza(self):
        pass

    @abstractmethod
    def make_premium_pizza(self):
        pass

    @abstractmethod
    def make_special_pizza(self):
        pass


class DominoPizza(AbstractPizzaStore):

    topings = ['cheeze', 'pepperoni', 'pimento',
               'potato', 'beef', 'bacon', 'shrimp',
               'lobster', 'caviar']

    def make_simple_pizza(self):
        return SimplePizza('just domino pizza', 10000, self.topings[:3])

    def make_premium_pizza(self):
        return PremiumPizza('good domino pizza', 20000, self.topings[:7])

    def make_special_pizza(self):
        return SpecialPizza('nice domino pizza', 100000, self.topings)


class PizzaHut(AbstractPizzaStore):

    topings = ['cheeze', 'pepperoni', 'potato',
               'pimento', 'beef', 'bacon', 'shrimp',
               'lobster']

    def make_simple_pizza(self):
        return SimplePizza('Hut happy', 15000, self.topings[:4])

    def make_premium_pizza(self):
        return PremiumPizza('Hut premium', 30000, self.topings[:6])

    def make_special_pizza(self):
        return SpecialPizza('Hut special', 50000, self.topings)


class SimplePizza:

    def __init__(self, name, price, topings):
        self.name = name
        self.price = price
        self.topings = topings

    def describe(self):
        print(f"{self.name} contains {self.topings}. It`s price is {self.price}")


class PremiumPizza:

    def __init__(self, name, price, topings):
        self.name = name
        self.price = price
        self.topings = topings

    def describe(self):
        print(f"{self.name} contains {self.topings}. It`s price is {self.price}")


class SpecialPizza:

    def __init__(self, name, price, topings):
        self.name = name
        self.price = price
        self.topings = topings

    def describe(self):
        print(f"{self.name} contains {self.topings}. It`s price is {self.price}. Too expensive")


def main():
    domino = DominoPizza()
    hut = PizzaHut()

    domino_simple = domino.make_simple_pizza()
    domino_simple.describe()
    domino_premium = domino.make_premium_pizza()
    domino_premium.describe()
    domino_special = domino.make_special_pizza()
    domino_special.describe()

    hut_simple = hut.make_simple_pizza()
    hut_simple.describe()
    hut_premium = hut.make_premium_pizza()
    hut_premium.describe()
    hut_special = hut.make_special_pizza()
    hut_special.describe()


if __name__ == "__main__":
    main()
