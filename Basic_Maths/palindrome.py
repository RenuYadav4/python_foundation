from primeNumber import prime_number
# after reversing a number it gives the origial number
def palindrome(n):
    temp = n
    rev = 0
    while(temp>0):
        digit = temp%10
        rev = rev * 10 + digit  
        temp = temp//10  
    if rev == n:
        return True
    else:
        False

num = int(input("Enter the number"))
if palindrome(num):
    print(f"{num} is palindrome")
else:
    print(f"{num} is not palindrome")



# this is also the function for finding the palindrome
# def is_palindrome(n):
#     return str(n) == str(n)[::-1]

def is_prime_palindrome(n):
    return prime_number(n) and palindrome(n)

primpalindrome = is_prime_palindrome(num)

print(primpalindrome,'primePalindrome')