Python is a case sensitive language.


# STring - operations

strings are immutable 

1. concatenation : "hello" + "world" = helloworld

2. lenght of str : len(str)

3. indexing is also there in python. (negative indexing is also there.)

4. Slicing  : accessing parts of a string
    - str[starting_idx : ending_idx] #ending idx is not included

# Conditional statement
if, elif, else


# LIst: 
- Mutable  (unlike strings)
- allows mixed types
- indexing 
- grow in size
- slicing allowed ; (same as string ) based on negative and positive index both.
- assignment is allowed


# methods in list
append()
sort()
reverse()
insert(idx,el)


# Tuples
- immutable
- paranthesis ()
- indexing
- direct assignment is not allowed like string
- slicing (same as list and string)


# Methods in tuples
tup.index(el)
tup.count(1)  ... and more


# Dictionary 
- key value pairs
- unordered, mutable
- no copy keys are allowed
- can store list, tuples also 
- no indexing 
- access elememts through key name
- nested dictionaries allowd

# SEt

- it mutable but its elements are not mutable
- store values , {1,2,32,2,"renu"}
- repeated values stored only once 


# loops
- while
- for 

# pass
 pass is a null statement that does nothing. It is used as a placeholder for future  code.

 for el in nums:
    pass

other code /


# Function

block of statements that perform a specific task.
- to avoid reduncdancy in our code


<!--function defintion -->
def func_name(param1, param2..):
    #some work
    return val

<!-- function call -->
func_name(arg1, arg2...)

<!-- if no arguments are passed, give your function default parameters they will be used in case when no arguments are passed -->



# Recursion
loops and recursion are interrelated.
means they both can do each other's task.
- base case is must to stop the recursion function
- call stack = multiple function calls 


# File input/output in python

types of files : 
1. Text Files : .txt, .docx, .log etc.
2. Binary Files : mp4, .mov, .png, .jpeg etc.


# Opps in Python

<!-- class and object  -->
class is a blueprint , 
object is the inctance of the class


<!-- constructor -->
All classees have a function called _init_(), which is always executed when the class is being initiated or instanciated.

# creating class
    class Student:
       def  __init__(self, fullname);
           self.name = fullname

# creating object
   s1 = Student("Karan")
   print(s1.name)

*The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.


# Inheritance 
properties inherited from father
keyword : super() -> points to the parent class

# Encapsulation
bind data and functions together to hide the data by making them private ,
getter and setter are used

to make an attribute private use __variable ,

class can access the private attribute but an object can not it need to use getter to access the private attribute


# Polymorphism

-ek method anek roop dharan kar skta hai
- two forms of polymorphisms:
1. method overridding(Runtime polymorphism) -> class changes the behaviour of parent class. same function different behavious based on object.

2. mothed overloading(compiletime polymoorphism) -> same function name, different parameters

python does not support true overloading like java/c++, but we simulate it.

# class variable

1. common class variable which directly related class and accessed directly by the class without the object
2. example : total_car , total number of object of the class Car, will be accessed as Car.total_car


# Static Method 
1. Belongs to the class directly rather than the object of the class.
2. Can be called without the instance( object) of the class
3. Available only to the class not the instance of that.

Stops the method to call using class
example :  in above topic, we should not be able to access total_car from the object (obj.total_car): we can use static_method in this case.

4. decorator : @staticmethods is used to make anything static.


# Property decorator
- makes a variable read only
- stops varibale to be overwritten.
- that variable can not be overwritten later by anyone.

- use a method to access that variable.

# isinstance()
tells if an object belonngs to a class of not


# Python supports multiple inheritance
