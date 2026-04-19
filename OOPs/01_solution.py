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

my_car= Car("Toyota","Corolla")
print(my_car.brand)
print(my_car.model)

print(my_car.full_name())

