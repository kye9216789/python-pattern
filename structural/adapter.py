from abc import ABC, abstractmethod


class Numerical_adder:
    addable = (int, float)

    def checker(self, data):
        return isinstance(data, self.addable)

    def __call__(self, args):
        return sum(args)

class String_concater:
    concatable = (str)

    def checker(self, data):
        return isinstance(data, self.concatable)

    def __call__(self, args):
        return "".join(args)


class Adapter:
    def __init__(self, operation):
        assert hasattr(operation, "checker")
        self.op = operation

    def operate(self, args):
        new_arg = []
        for arg in args:
            if self.op.checker(arg):
                new_arg.append(arg)
        print(new_arg)
        return self.op(new_arg)


def main():
    param = [1, 2, "3", 4, "5", 6, "seven"]
    try:
        print(sum(param))
    except:
        print("Can not add parameters")

    add_adapter = Adapter(Numerical_adder())
    concat_adapter = Adapter(String_concater())

    try:
        print(add_adapter.operate(param))
    except:
        print("Adapter also failed to add parameters")


    try:
        print("".join(param))
    except:
        print("Can not concatenate numbers")

    print(concat_adapter.operate(param))
    try:
        print(concat_adapter.operate(param))
    except:
        print("Adapter also failed to concat parameters")


if __name__ == "__main__":
    main()
