print("Hello World")

# variables
name = "Renu"  #string
age = 22       #integer
price = 25.99   # floating number

print(name)
print("my name is:", name)

old = False
a = None
print(type(old))
print(type(a))

a= 2
b = 5
sum = a+b
print(sum)


# Operators
# Arithmetic, Relational, Assignment,  Logical

val1 = True
val2 = False

print("AND Operator:", val1 and val2 )
print("OR operator:", val1 or val2)

print("Or operator:", (a==b)or(a>b))

#1. Type conversion -> python automatically does
# 2. Type Casting ->manually forcfully done using function 

c= 2
d = 4.25 
print(type(c))   #int
print(c+d);  #python type casts to superior one here (i.e. float)


c=int("2")
print(type(c))    #int
print(c+d);   #Type casting , done forcefully.


# Taking input in python
name = input("Enter your name:")    #input return string bydefault, use typecasting for another type
print("welcome ",name)

name = int(input("Enter your name:") )
print(type(name))