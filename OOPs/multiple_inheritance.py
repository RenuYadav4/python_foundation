class Car:
    
    def __init__(self,brand,model):  
        self.model = model
        self.__brand = brand

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
         

class Battery:
    def battery_info(self):
        return "this is battery"
    

class Engine:
    def engine_info(self):
        return "this is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "model S")
print(my_new_tesla.engine_info)
print(my_new_tesla.battery_info())
