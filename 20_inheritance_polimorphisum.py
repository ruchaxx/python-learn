#inheritance
class Animal():
    def __init__(self):
        print("animal created")
    def who_m_i(self):
        print("cow")
    def eat(self):
        print("eatting")

animal = Animal()

class Dog(Animal):
    def __init__(self):
        Animal().__init__()
        print("dog created")
    def who_m_i(self):
        print("i am dog")
    def bark(self):
        print("woof")

dog = Dog()
dog.who_m_i()

#polymorphism
class Dogs():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " sayss woof"
class Cat():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " sayss meow"

niko = Dogs('niko')
kitty = Cat('kitty')
print(niko.speak())
print(kitty.speak())

for pet in [niko,kitty]:
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())

print(pet_speak(niko))


#abstract class (aano instance nai hoy)
class Animal():
    def __init__(self,name):
        self.name = name
    def speak(self):
        raise NotImplementedError("subclass must implememnted abstarct method")
class Dog(Animal):
    def speak(self):
        return self.name + " woof"
class Cat(Animal):
    def speak(self):
        return self.name + " meow"
fido = Dog('fido')
print(fido.speak())
isis = Cat('isis')
print(isis.speak())
