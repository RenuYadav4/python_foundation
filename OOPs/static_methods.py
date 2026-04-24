# Question : Add a static method to the Car class that returns a general description of a car.
class Car:
    total_car = 0

    def __init__(self,brand,model):  
        self.model = model
        self.__brand = brand
        Car.total_car += 1
    
    
    # getter for brand attribute
    def get_brand(self):
        return self.__brand+" !" 
          
    # setter for brand attribute
    def set_brand(self,new_brand):
        if new_brand:
            self.__brand = new_brand
        else:
            print("INvalid brand!")
        
    # POlymorphism implements 
    def fuel_type(self):
        return "Petrol or Diesel"
         
    @staticmethod  #decorators
    def general_description():
        return "Cars are means of transport"


# creating objects without reference
my_car = Car("tata", "Safari")
Car("Tata", "Nexon")

print(Car.total_car)
# print(my_car.general_description())  it should not access static method
print(my_car.general_description())