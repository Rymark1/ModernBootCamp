class Chicken:

    total_eggs = 0

    def __init__(self, species, name, eggs=0):
        self.species = species
        self.name = name
        self.eggs = eggs

    def lay_egg(self):
        Chicken.total_eggs += 1


c1 = Chicken(name="Alice", species="Partridge Silkie")
c2 = Chicken(name="Amelia", species="Speckled Sussex")
Chicken.total_eggs #0
c1.lay_egg()  #1
Chicken.total_eggs #1
c2.lay_egg()  #1
c2.lay_egg()  #2
Chicken.total_eggs #3