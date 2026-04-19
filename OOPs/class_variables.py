# Question : Add a class variable to Car that keeps track of the number of cars created.
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
         
    
    def full_name(self):
        return f"{self.__brand} {self.model}"


# creating objects without reference
Car("tata", "Safari")
Car("Tata", "Nexon")

print(Car.total_car)
