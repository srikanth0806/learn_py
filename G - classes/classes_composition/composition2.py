"        '  COMPOSITION OF CLASSES '             "
class Bird():

    def __init__(self, colour, special):
        self.colour = colour
        self.special = special

    def get_colour(self):
        return self.colour

    def set_colour(self, new_colour):
        self.colour = new_colour

    def get_special(self):
        return self.special

    def set_special(self, new_special):
        self.colour = new_special


class parrot:
    def __init__(self, colour, special):
        self.Bird_object = Bird(colour, special)

    def get_colour(self):
        return self.Bird_object.colour

    def get_special(self):
        return self.Bird_object.special

    def set_special(self, new_special):
        self.Bird_object.special = new_special


x = parrot("green", "talking")
print(x.get_colour())
x.set_special("dancing")
print(x.get_special())

