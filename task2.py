class Vehicle():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
         
    def show_info(self):
        raise NotImplementedError("Bunday metod hali mavjud emas!")

class Car(Vehicle):
    def show_info(self):
        print(f"Car: {self.brand}, {self.model}, {self.year}")

class Bike(Vehicle):
    def show_info(self):
        print(f"Bike: {self.brand}, {self.model}, {self.year}")


car = Car("Chevrolet", "gentra", 2022)
bike = Bike("desna", "Domane", 2022)


car.show_info()
bike.show_info()

