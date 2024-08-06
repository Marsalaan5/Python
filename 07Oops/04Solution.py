class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !"

    
    def full_name(self):
        return f"{self.__brand} {self.model} {self.battery_capacity}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity


my_tesla = ElectricCar("Tesla","Model S","85kWH")
# print(my_tesla.__brand)
print(my_tesla.get_brand())





# my_Car = Car("Toyota","Cororlla")
# print(my_Car.brand)
# print(my_Car.model)
# print(my_Car.full_name())


# my_new_Car = Car("Tata","Safari")
# print(my_new_Car.brand)
# print(my_new_Car.model)