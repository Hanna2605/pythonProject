class Furniture:
    def __init__(self, height, width, length):
       self.height = height
       self.width = width
       self.length = length

    def square(self):
        return self.width * self.length

    def volume(self):
        return self.height * self.width * self.length

    def __add__(self, other):
        return self.square + other.square

class Table(Furniture):
    def __init__(self, material):
        self.material = material

class Bed(Furniture):
    def __init__(self, material):
        self.material = material
