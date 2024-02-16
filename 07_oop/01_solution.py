class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota","Supra")
print(my_car.brand,my_car.model)

my_new_car = Car("Tata","Safari")
print(my_new_car)
print(my_new_car.brand,my_new_car.model)