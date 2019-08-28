from abc import ABC, abstractmethod


class AbstractSeller(ABC):

    def accept(self, visitor):
        visitor.visit(self)


class BreadSeller(AbstractSeller):

    def __init__(self):
        self.money_earned = 0
        self.bread_price = 5000


class PhoneSeller(AbstractSeller):

    def __init__(self):
        self.money_earned = 500000
        self.phone_price = 1000000


class AbstractVisitor(ABC):

    def visit(self, seller):
        if isinstance(seller, BreadSeller):
            self.visit_bread(seller)
        elif isinstance(seller, PhoneSeller):
            self.visit_phone(seller)

    @abstractmethod
    def visit_bread(self, seller):
        pass

    @abstractmethod
    def visit_phone(self, seller):
        pass


class Buyer(AbstractVisitor):

    def __init__(self, money=10000):
        self.money = money
        self.num_goods = 0

    def visit_bread(self, seller):
        if seller.bread_price < self.money:
            self.money -= seller.bread_price
            seller.money_earned += seller.bread_price
            self.num_goods += 1
            print("I bought bread.")
        else:
            print("Too expensive. I don`t have enought money.")

    def visit_phone(self, seller):
        if seller.phone_price < self.money:
            self.money -= seller.phone_price
            seller.money_earned += seller.phone_price
            self.num_goods += 1
            print("I bought a cell phone.")
        else:
            print("Too expensive. I don`t have enought money.")


class Gangster(AbstractVisitor):

    def __init__(self):
        self.money = 0

    def visit_bread(self, seller):
        if seller.money_earned > 0:
            self.money += seller.money_earned // 10
            seller.money_earned -= seller.money_earned // 10
            print(f"I just took tax : {seller.money_earned // 10}.")
        else:
            print("You don`t have money.")

    def visit_phone(self, seller):
        if seller.money_earned > 0:
            self.money += seller.money_earned // 5
            seller.money_earned -= seller.money_earned // 5
            print(f"I just took tax : {seller.money_earned // 5}.")
        else:
            print("You don`t have money.")


def main():

    poor = Buyer(1000)
    rich = Buyer(100000000)

    gangster = Gangster()

    bread_seller = BreadSeller()
    phone_seller = PhoneSeller()

    bread_seller.accept(gangster)
    phone_seller.accept(gangster)

    bread_seller.accept(poor)
    phone_seller.accept(rich)

    bread_seller.accept(gangster)
    phone_seller.accept(gangster)



if __name__ == "__main__":
    main()
