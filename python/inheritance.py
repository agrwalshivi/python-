# Simple Inheritance

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

# Create an instance of Dog
dog = Dog()
# Call the sound method of Dog
dog.sound()

#multiple inheritance
# Parent class 1
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

# Parent class 2
class Flyable:
    def fly(self):
        print("I can fly!")

# Child class inheriting from both Animal and Flyable
class Bird(Animal, Flyable):
    def speak(self):
        print(f"{self.name} says: Chirp chirp!")

# Child class inheriting from both Animal and Flyable
class Bat(Animal, Flyable):
    def speak(self):
        print(f"{self.name} says: Screech screech!")

# Create instances of Bird and Bat
parrot = Bird("Parrot")
bat = Bat("Bat")

# Call methods of Bird and Bat
parrot.speak()  # Output: Parrot says: Chirp chirp!
parrot.fly()    # Output: I can fly!
bat.speak()     # Output: Bat says: Screech screech!
bat.fly()       # Output: I can fly!
