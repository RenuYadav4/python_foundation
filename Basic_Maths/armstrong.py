def armstrong(n1):
    temp = n1
    length = len(str(temp))
    sum_of_pow = 0
    while(temp>0):
        digit = temp%10
        sum_of_pow = sum_of_pow+(digit**length)
        temp = temp//10
       
    if n1 == sum_of_pow:
        print(f"{n1} is an Armstrong number")
    else:   
        print(f"{n1} is not an Armstrong number")

n1 = int(input("Enter the number:"))
armstrong(n1)


#  using recursion
def armstrong_recursive(n,length):
    if n==0:
        return 0
    digit = n%10
    return (digit**length) + armstrong_recursive(n//10, length)

def check_recursive(num1):
    length = len(str(num1))
    result = armstrong_recursive(num1, length)

    if result == num1:
        print(f"{num1} is an Armstrong number")
    else:
        print(f"{num1} is not an Armstrong number")

num1 = int(input("Enter the number for recursive:"))
check_recursive(num1)