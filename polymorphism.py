# Define a base class 'Animal'
class Animal:
    def __init__(self, name):
        self.name = name

    # Abstract method (does not have body)
    def sound(self):
        pass

# Define subclasses 'Dog' and 'Cat', both inheriting from 'Animal'
class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

# Create instances of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Use polymorphism to call the sound() method on each instance
print(dog.sound())  # Output: Woof!
print(cat.sound())  # Output: Meow!

# Polymorphism allows us to treat these instances interchangeably when they are of the same type (Animal),
# even though they may behave differently.
