def gcd(n1,n2):
    gcd = 1
    for i in range(1, min(n1,n2)+1):
        if n1%i == 0 and n2%i == 0:
            gcd = i
    return gcd


num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

result = gcd(num1,num2)
print(f"gcd of {num1} and {num2} is {result}")

# better approach
def gcd_better(n1,n2):
    gcd = 1
    for i in range(min(n1,n2),0,-1):
        if n1%i == 0 and n2%i==0:
            gcd = i
            return gcd   #returns immediately 
   

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

result = gcd_better(num1, num2)

    
print(f"the result of optised gcd approach. And the greatest common divisor of {num1} and {num2} is {result}")