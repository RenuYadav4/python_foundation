# question 1: print the nth fibonacci number 
def iterative_fibonumber(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a,b =0,1
    for i in range(2, n+1):
        a, b = b, a+b

    return b

n = 9
print(f"The fibonacci number at position {n} is {iterative_fibonumber(n)}")

# Question 2: print nth fibonacci number using recusrion
# iterative is better, becuase in recursive approach multiple repeated calls.
#  It first goes into f(n-1) deeply,
# reaches base case, starts returning,
# then f(n-2) is called, goes deep,
# returns value, and both are added.
# This is correct, but understand when f(n-2) is called.
# It actually happens at every level, not just once.

def recursive_fibonumber(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return recursive_fibonumber(n-1) + recursive_fibonumber(n-2)


# Question 3: print the whole fibonacci series using iterative 
def fibonacci_series(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]

    series = [0, 1]

    for i in range(2, n):
        series.append(series[-1] + series[-2])  # last and seccond last element using negative indexing
        # series[len(series)-1] + series[len(series)-2]  without negative indexing

    return series


print(fibonacci_series(5))


