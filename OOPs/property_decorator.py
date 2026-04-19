#Question: Use the property decorator in a class Car to make the modal attribute read-only.

class Car:
    
    def __init__(self,brand,model):  
        self.__model = model  #modal should be private now
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

    # method to access modal
    @property
    def model(self):
        return self.__model


