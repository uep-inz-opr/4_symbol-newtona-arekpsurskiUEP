from math import factorial
def binomial(a,b):
    return factorial(a) // factorial(b) // factorial(a-b)
a, b = map(int, input().split())
print(binomial(a,b))