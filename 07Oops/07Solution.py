class Car:

    total_car = 0

    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        # self.total_car += 1
        Car.total_car += 1


    def get_brand(self):
        return self.__brand + " !"

    
    def full_name(self):
        return f"{self.__brand} {self.model} {self.battery_capacity}"
    

    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def gen_desc():
        return "This is a car description"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def fuel_type(self):
        return "Electric Charge"


# my_tesla = ElectricCar("Tesla","Model S","85kWH")
# print(my_tesla.__brand)
# print(my_tesla.get_brand())
# print(my_tesla.fuel_type())

my_car = Car("Tata","Safari")
Car("Tata","Nexon")


print(my_car.gen_desc())
print(Car.gen_desc())






# my_Car = Car("Toyota","Cororlla")
# print(my_Car.brand)
# print(my_Car.model)
# print(my_Car.full_name())


# my_new_Car = Car("Tata","Safari")
# print(my_new_Car.brand)
# print(my_new_Car.model)