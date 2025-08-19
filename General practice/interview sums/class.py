class Animal:
    def __init__(self, name, spices):
        self.name = name
        self.spices = spices
    def fullName(self, breed):
        self.breed = breed
        return f'{self.name} the {self.breed} {self.spices}'
    
class Dog(Animal):
    def __init__(self, foodType):
        self.foodType = foodType
    def fullDesc(self, name, spices, breed):
        super().__init__(name, spices)
        return f'{name} the {breed} {spices} with {self.foodType} food choice'

    
dog = Dog('Carnivore')
print(dog.fullDesc('Kevin', 'Rottwiller', 'Dog'))

