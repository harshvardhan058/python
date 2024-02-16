class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model 

    def get_brand(self):
        return self.__brand
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    @staticmethod
    def general_description():
        return "Cars are good way to transport and also comfortable"
    
my_car = Car("tata","safari")

print(Car.general_description())