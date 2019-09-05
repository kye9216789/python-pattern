from abc import ABC, abstractmethod


class PhoneBuilder(ABC):

    def __init__(self):
        self.phone = {}

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_memory(self):
        pass

    @abstractmethod
    def set_display_type(self):
        pass

    @abstractmethod
    def set_spen(self):
        pass

    def get_result(self):
        return self.phone


class GalaxySBuilder(PhoneBuilder):

    def __init__(self):
        super().__init__()
        self.reset()

    def reset(self):
        self.phone["name"] = 'Galaxy S'

    def set_memory(self, size):
        self.phone["memory"] = size

    def set_display_type(self, display_type):
        self.phone["display"] = display_type

    def set_spen(self):
        print("Galaxy S does not supports S pen.")


class GalaxyNoteBuilder(PhoneBuilder):

    def __init__(self):
        super().__init__()
        self.reset()

    def reset(self):
        self.phone["name"] = 'Galaxy Note'

    def set_memory(self, size):
        self.phone["memory"] = size

    def set_display_type(self, display_type):
        self.phone["display"] = display_type

    def set_spen(self):
        self.phone["pen"] = "S-pen"


class SamsungMobile:
    galaxy_s_builder = GalaxySBuilder()
    galaxy_note_builder = GalaxyNoteBuilder()

    def make_galaxy_s(self):
        self.galaxy_s_builder.set_memory(6)
        self.galaxy_s_builder.set_display_type("LCD")
        self.galaxy_s_builder.set_spen()
        return self.galaxy_s_builder.get_result()

    def make_galaxy_note(self):
        self.galaxy_note_builder.set_memory(12)
        self.galaxy_note_builder.set_display_type("AMOLED")
        self.galaxy_note_builder.set_spen()
        return self.galaxy_note_builder.get_result()


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
