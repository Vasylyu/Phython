


class Pets:
    def __init__(self, dods, cats, hamsters):
        self.dogs = dods
        self.cats = cats
        self.hamsters = hamsters
    pass

class Pack_animals:
    def __init__(self, horses, camels, donkeys):
        self.horses = horses
        self.camels = camels
        self.donkeys = donkeys

    pass


class Names_animals(Pack_animals, Pets):
    def __init__(self, names, comands, date_of_birth):
        self.names = names
        self.comands = comands
        self.date_of_birth = date_of_birth
    pass