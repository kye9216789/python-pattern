from abc import ABC, abstractmethod


class AbstractPizzaStore(ABC):

    @abstractmethod
    def make_original_pizza(self):
        pass

    @abstractmethod
    def make_premium_pizza(self):
        pass

    @abstractmethod
    def make_special_pizza(self):
        pass


class DominoPizza(AbstractPizzaStore):

    toppings = ['cheese', 'pepperoni', 'pimento',
               'potato', 'beef', 'bacon', 'shrimp',
               'lobster', 'caviar']

    def make_original_pizza(self):
        return OriginalPizza('just domino pizza', 10000, self.toppings[:3])

    def make_premium_pizza(self):
        return PremiumPizza('good domino pizza', 20000, self.toppings[:7])

    def make_special_pizza(self):
        return SpecialPizza('nice domino pizza', 100000, self.toppings)


class PizzaHut(AbstractPizzaStore):

    toppings = ['cheese', 'pepperoni', 'potato',
               'pimento', 'beef', 'bacon', 'shrimp',
               'lobster']

    def make_original_pizza(self):
        return OriginalPizza('Hut happy', 15000, self.toppings[:4])

    def make_premium_pizza(self):
        return PremiumPizza('Hut premium', 30000, self.toppings[:6])

    def make_special_pizza(self):
        return SpecialPizza('Hut special', 50000, self.toppings)


class OriginalPizza:

    def __init__(self, name, price, toppings):
        self.name = name
        self.price = price
        self.toppings = toppings

    def describe(self):
        print(f"{self.name} contains {self.toppings}. It`s price is {self.price}")


class PremiumPizza:

    def __init__(self, name, price, toppings):
        self.name = name
        self.price = price
        self.toppings = toppings

    def describe(self):
        print(f"{self.name} contains {self.toppings}. It`s price is {self.price}")


class SpecialPizza:

    def __init__(self, name, price, toppings):
        self.name = name
        self.price = price
        self.toppings = toppings

    def describe(self):
        print(f"{self.name} contains {self.toppings}. It`s price is {self.price}. Too expensive")


def main():
    domino = DominoPizza()
    hut = PizzaHut()

    domino_simple = domino.make_original_pizza()
    domino_simple.describe()
    domino_premium = domino.make_premium_pizza()
    domino_premium.describe()
    domino_special = domino.make_special_pizza()
    domino_special.describe()

    hut_simple = hut.make_original_pizza()
    hut_simple.describe()
    hut_premium = hut.make_premium_pizza()
    hut_premium.describe()
    hut_special = hut.make_special_pizza()
    hut_special.describe()


if __name__ == "__main__":
    main()
