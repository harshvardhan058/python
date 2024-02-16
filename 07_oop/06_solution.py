class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_first_car = Car("test1","test1")
my_second_car = Car("test2","test2")
my_third_car = Car("test3","test3")
my_fourth_car = ElectricCar("test4","test4","test4")

print(Car.total_car)


    