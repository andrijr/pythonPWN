# P57
# Napisz program implementujący funkcję n! - silnia

def factorial(n):
    result = 1
    if(n<0):
        return "Error"
    if(n == 0):
        return 1
    for i in range(2, n+1):
        result *= i
    return result

print(factorial(4))
print(factorial(0))
print(factorial(-5))

# Rekurencyjnie
def factorialRec(n):
    if(n == 1):
        return 1
    return n * factorialRec(n-1)