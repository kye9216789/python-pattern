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


class MobilePhoneTeam:

    def set_production_line(self, production_line, pd_cfg):
        production_line.set_memory(pd_cfg["memory"])
        production_line.set_display_type(pd_cfg["display"])
        if "pen" in pd_cfg.keys():
            production_line.set_spen(pd_cfg["pen"])
        return production_line


def main():
    director = MobilePhoneTeam()

    galaxy_s_order = {
        "memory":6,
        "display":"LCD"
    }

    galaxy_note_order = {
        "memory":8,
        "display":"AMOLED",
        "pen":"S-pen"
    }

    galaxy_s_line = director.set_production_line(
        GalaxySProductionLine(),
        galaxy_s_order
    )
    galaxy_note_line = director.set_production_line(
        GalaxyNoteProductionLine(),
        galaxy_note_order
    )

    galaxy_s = galaxy_s_line.get_product()
    galaxy_note = galaxy_note_line.get_product()

    for k in galaxy_s.keys():
        print(f'{k}: {galaxy_s[k]}')

    for k in galaxy_note.keys():
        print(f'{k}: {galaxy_note[k]}')


if __name__ == "__main__":
    main()
