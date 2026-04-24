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
            return gcd   #returns immediately (because in first iteration we get greatest value as we are running opposite loop) or we can return i directly.
   
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

result = gcd_better(num1, num2)

    
print(f"the result of optised gcd approach. And the greatest common divisor of {num1} and {num2} is {result}")


# optimal approach : Euclidean Algorithm
# The Euclidean Algorithm is a method for finding the greatest common divisor (GCD)
# of two numbers. It operates on the principle that the GCD of two numbers remains
# the same even if the smaller number is subtracted from the larger number.

# To find the GCD of n1 and n2 where n1 > n2:
# 1. Repeatedly subtract the smaller number from the larger number until one of them becomes 0.
# 2. Once one becomes 0, the other is the GCD of the original numbers.

def gcd_optimal(n1, n2):
    while n1 > 0 and n2 > 0:
        if n1 > n2:
            n1 = n1 - n2
        else:
            n2 = n2 - n1

    return n1 if n1 != 0 else n2

result = gcd_optimal(num1,num2)
print(f"the gcd from euclidean algo for {num1} and {num2} is {result}")
