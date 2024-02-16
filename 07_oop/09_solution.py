class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model

        @property
        def brand(self):
            return self.__brand
        
        @property
        def model(self):
            return self.__model
        
        def full_name(self):
            return f"{self.__brand} {self.__model}"
        
        @staticmethod
        def general_description():
            return "Car is a car nothing Else but the person who loves the car then for him the car has some other thing"
        
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size



my_car = Car("Toyota","Supra")
print(isinstance(my_car,Car))
print(isinstance(my_car,ElectricCar))

my_ev_car = ElectricCar("Tesla","Model x","85kWh")

print(isinstance(my_ev_car,Car))
print(isinstance(my_ev_car,ElectricCar))
