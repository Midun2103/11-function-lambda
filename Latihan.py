import math
#   Midun Hakiki 22ITB1


def a(n): return lambda x: x**n


lambdaA = a(4)
print(lambdaA(4))


def b(i, j):
    return lambda x, y: math.sqrt(x**i + y**j)
    

lambdaB = b(4, 0)
print(lambdaB(3, 0))


def c(*args):
    return lambda *params: sum(args) / len(params)
    

lambdaC = c(1, 2, 3, 4, 5)
print(lambdaC(2, 5))


def d(firstname):
    return lambda *lastname: "".join(set(firstname)) + "".join(set(lastname))


lambdaD = d ("Midun")
print(lambdaD("Hakiki"))

