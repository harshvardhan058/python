class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model

    @staticmethod
    def general_description():
        return "simple Car"
    
    @property
    def model(self):
        return self.__model
    
my_car = Car("BMW","class 1")
print(my_car.model)