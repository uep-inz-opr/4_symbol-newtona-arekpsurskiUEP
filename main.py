from math import factorial
def binomial(a,b):
    return factorial(a) // factorial(b) // factorial(a-b)
a = int(input())
b = int(input())
print(binomial(a,b))