from abc import ABC, abstractmethod


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance



def main():
    a = Singleton()
    b = Singleton()

    print(f'ID of first instance : {id(a)}')
    print(f'ID of second instance : {id(b)}')


if __name__ == "__main__":
    main()
