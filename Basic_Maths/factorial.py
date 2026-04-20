def iterative_fact(n):
    if n <= 0:
        return "invalid input"
    
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def recursive_fact(n):
    if n==1 or n==1:
        return 1
    return n*recursive_fact(n-1)

print("iterative",iterative_fact(5))
print("recursive",recursive_fact(5))


