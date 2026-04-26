# The code idea
# so the idea is we can find factor of the number it should have only two factors 1 and itself
# and we find factor til root of n , because after that factors starts repeating.and can not be greater then n.

# “Factors never exceed the number, and for checking, we only need to go till √n.”
def prime_number(n):
    if n<=1:
        return False
    for i in range( 2,int(n**0.5)+1):   #👉 Converts that float into an integer (removes decimal part). 2. if we would have use n instesd of root n then we can ignore +1, but here in root we should check for root also
#         We never go till n
# We only go till √n
# +1 is just to include √n, not to reach n
        if n%i == 0:
            return False
        
    return True

if __name__ == "__main__":
   num = int(input("Enter a number"))    
   result = prime_number(num)
   if (result == True):
      print(f"{num}  is prime")

   else:
      print(f"{num} is not prime")