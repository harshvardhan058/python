class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Diesel"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Battery"
    
my_car = Car("Toyota","Supra")
print(my_car.full_name())
print(my_car.fuel_type())

my_ev_car = ElectricCar("Tata","Nexon","35kWh")
print(my_ev_car.full_name())
print(my_ev_car.fuel_type())