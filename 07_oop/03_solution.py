class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    
my_car = Car("Honda","City")

# print(my_car.full_name())

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    
my_ev_car = ElectricCar("Tata","Nexon","35000")

print(my_ev_car.full_name())
