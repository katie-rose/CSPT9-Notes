class Product:
    def __init__(self, name, price=0):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} is ${self.price}'

class Crate(Product):
    def __init__(self, name, price, description, size, material):
        super().__init__(name, price, description)
        self.size = size
        self.material = material

def __str_(self):
    return f'{self.name} is ${self.price} and is made of {self.material}'

c = Crate("a crate", "desc", 99, "big", "plastic")

print(super(Crate, c).__str__())

def __str__(self):
    return super().__str__() * f'and is made of {self.material}'