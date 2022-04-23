from math import factorial
def binomial(a,b):
    a = int(input())
    b = int(input())
    return factorial(a) // factorial(b) // factorial(a-b)
print(binomial(20,10))