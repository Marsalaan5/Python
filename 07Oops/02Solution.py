class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    
    def full_name(self):
        return f"{self.brand} {self.model}"

my_Car = Car("Toyota","Cororlla")
print(my_Car.brand)
print(my_Car.model)
print(my_Car.full_name())


my_new_Car = Car("Tata","Safari")
print(my_new_Car.brand)
print(my_new_Car.model)