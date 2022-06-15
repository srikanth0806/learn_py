from abc import ABC, abstractmethod


class Bird:

    def __init__(self, colour):
        self.colour = colour

    @abstractmethod
    def get_colour(self):
        pass

    @abstractmethod
    def set_colour(self):
        pass


class parrot(Bird):
    def get_colour(self):
        return self.colour

    def set_colour(self, colour):
        self.colour = colour


x = parrot("green")
print(x.get_colour())
