class Person():
    def __init__(self, name):
        self.name = name

    def print(self):
        print(self.name)


hunter = Person("Elmer Fudd")
magician = Person("Gundulf")

hunter.print()
magician.print()
