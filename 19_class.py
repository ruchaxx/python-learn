class Sample():
    pass
my_sample = Sample()
print(type(my_sample))

class Dog():
    def __init__(self,bread,name,sports):
        self.bread = bread #string
        self.name = name #string
        self.sports = sports #bool

my_dog = Dog(bread='lab', name = 'sammy',sports=False)
print(my_dog.bread)
print(my_dog.name)
print(my_dog.sports)


class Dog():

    #class object attribute
    #same for any instance of calss
    species = 'mammal'
    def __init__(self,bread,name,sports):
        self.bread = bread #string
        self.name = name #string
        self.sports = sports #bool

    #methods --> fuctions inside class
    def bark(self,num):
        print("woof name is {} and number is {}".format(self.name,num))

my_dog = Dog(bread='lab', name = 'sammy',sports=False)
print(my_dog.species)
my_dog.bark(4)


class Circle():
    pi = 3.14
    def __init__(self,r=1):
        self.r = r
    def cirecumferance(self):
        return 2 * self.pi * self.r

my_circle = Circle(100)
print(my_circle.cirecumferance())