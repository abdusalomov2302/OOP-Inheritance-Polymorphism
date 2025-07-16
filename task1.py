
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError(" bunday metod mavjud emas!")


class Dog(Animal):
    def speak(self):
        return f"{self.name} Vov-vov-vov!"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} Miyovv!"
    
dog = Dog("jerry")
cat = Cat("tommy")

print(dog.speak())
print(cat.speak())