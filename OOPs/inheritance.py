# definging class Car with atttributes brand and model
class Car:
    
    # constructor
    def __init__(self,brand,model):   #self  points to the object which is calling Car class or getting created
        self.model = model
        self.brand = brand

# function with functionality to print full name 
    def full_name(self):
        # formatted string
        return f"{self.brand} {self.model}"


# creating an instance of Car()

# my_car= Car("Toyota","Corolla")
# print(my_car.brand)
# print(my_car.model)

# print(my_car.full_name())

#  Question : Create an ElectricCar class that inherits from the Car class and has an additional attribute
# ElectricCar is now inherting from Car
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    
my_tesla = ElectricCar("Tesla","Model S","85kWh")
print(my_tesla.full_name())
print(my_tesla.brand)
print(my_tesla.battery_size)
print(my_tesla.model)