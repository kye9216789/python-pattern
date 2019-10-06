from abc import ABC, abstractmethod


topping_dict = dict(
    cheese=500,
    kimchi=500,
    spam=1500,
    pickle=300,
    hot_source=300
)


class AbstractPrototypeFood(ABC):

    @abstractmethod
    def clone(self):
        pass

class Ramen(ABC):

    def __init__(self):
        super().__init__()
        self.type = 'noodle'
        self.price = 3000
        self.toppings = []

    def add_topping(self, topping):
        if topping not in self.toppings:
            self.toppings.append(topping)
            self.price += topping_dict[topping]
        else:
            print(f"{topping} is already added.")

    def clone(self):
        clone_ramen = Ramen()
        for topping in self.toppings:
            clone_ramen.add_topping(topping)
        return clone_ramen

    def __repr__(self):
        if len(self.toppings) > 0:
            return f"This ramen contains{self.toppings}"
        else:
            return f"This is basic ramen"


class FoodCourt:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_item_by_id(self, id):
        return self.items[id].clone()

    def get_item_by_price(self, price):
        for item in self.items:
            if item.price == price:
                return item.clone()
        print(f"There is no food for {price} won.")
        return None


def main():
    foodcourt = FoodCourt()

    basic_ramen_sample = Ramen()
    kimchi_ramen_sample = Ramen()
    kimchi_ramen_sample.add_topping("kimchi")

    foodcourt.add_item(basic_ramen_sample)
    foodcourt.add_item(kimchi_ramen_sample)

    order1 = foodcourt.get_item_by_id(0)
    print(order1)
    order2 = foodcourt.get_item_by_price(3500)
    print(order2)
    order3 = foodcourt.get_item_by_price(4000)
    print(order3)


if __name__ == "__main__":
    main()
