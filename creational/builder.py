from abc import ABC, abstractmethod


class AbstractProductionLine(ABC):

    def __init__(self, name):
        self.phone = {"name": name}

    @abstractmethod
    def set_spen(self):
        pass

    def set_memory(self, size):
        self.phone["memory"] = size

    def set_display_type(self, display_type):
        self.phone["display"] = display_type

    def get_product(self):
        return self.phone


class GalaxySProductionLine(AbstractProductionLine):

    def __init__(self):
        super().__init__("Galaxy S")

    def set_spen(self):
        pass


class GalaxyNoteProductionLine(AbstractProductionLine):

    def __init__(self):
        super().__init__("Galaxy Note")

    def set_spen(self, pen):
        self.phone["pen"] = pen


class PhoneShop:

    def __init__(self, production_line):
        self.production_line = production_line

    def make_phone(self, pd_cfg):
        self.production_line.set_memory(pd_cfg["memory"])
        self.production_line.set_display_type(pd_cfg["display"])
        if "pen" in pd_cfg.keys():
            self.production_line.set_spen(pd_cfg["pen"])


def main():

    galaxy_s_order = {
        "memory":6,
        "display":"LCD"
    }
    galaxy_note_order = {
        "memory":8,
        "display":"AMOLED",
        "pen":"S-pen"
    }

    galaxy_s_shop = PhoneShop(GalaxySProductionLine())
    galaxy_s_shop.make_phone(galaxy_s_order)
    galaxy_s = galaxy_s_shop.production_line.get_product()

    galaxy_note_shop = PhoneShop(GalaxyNoteProductionLine())
    galaxy_note_shop.make_phone(galaxy_note_order)
    galaxy_note = galaxy_note_shop.production_line.get_product()

    for k in galaxy_s.keys():
        print(f'{k}: {galaxy_s[k]}')

    for k in galaxy_note.keys():
        print(f'{k}: {galaxy_note[k]}')


if __name__ == "__main__":
    main()
