from abc import ABC, abstractmethod


class AbstractProductionLine(ABC):

    def __init__(self, name):
        self.phone = {"name": name}

    @abstractmethod
    def set_memory(self):
        pass

    @abstractmethod
    def set_display_type(self):
        pass

    @abstractmethod
    def set_spen(self):
        pass

    def get_product(self):
        return self.phone


class GalaxySProductionLine(AbstractProductionLine):

    def __init__(self):
        super().__init__("Galaxy S")

    def set_memory(self, size):
        self.phone["memory"] = size

    def set_display_type(self, display_type):
        self.phone["display"] = display_type

    def set_spen(self):
        print("Galaxy S does not supports S pen.")


class GalaxyNoteProductionLine(AbstractProductionLine):

    def __init__(self):
        super().__init__("Galaxy Note")

    def set_memory(self, size):
        self.phone["memory"] = size

    def set_display_type(self, display_type):
        self.phone["display"] = display_type

    def set_spen(self):
        self.phone["pen"] = "S-pen"


class MobilePhoneTeam:
    galaxy_s_line = GalaxySProductionLine()
    galaxy_note_line = GalaxyNoteProductionLine()

    def make_galaxy_s(self):
        self.galaxy_s_line.set_memory(6)
        self.galaxy_s_line.set_display_type("LCD")
        self.galaxy_s_line.set_spen()
        return self.galaxy_s_line.get_product()

    def make_galaxy_note(self):
        self.galaxy_note_line.set_memory(12)
        self.galaxy_note_line.set_display_type("AMOLED")
        self.galaxy_note_line.set_spen()
        return self.galaxy_note_line.get_product()


def main():
    director = SamsungMobile()
    galaxy_s = director.make_galaxy_s()
    galaxy_note = director.make_galaxy_note()

    for k in galaxy_s.keys():
        print(f'{k}: {galaxy_s[k]}')

    for k in galaxy_note.keys():
        print(f'{k}: {galaxy_note[k]}')


if __name__ == "__main__":
    main()
