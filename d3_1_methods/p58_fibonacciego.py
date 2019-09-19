# P58
# Napisz program obliczający wartość zadanego elementu ciągu Fibonacciego i obliczający sumę elementów ciągu.
# Fibonacciego

# Napisz program obliczający wartość zadanego elementu ciągu Fibonacciego i obliczający sumę elementów ciągu.
# 0, 1,1,2,3,5,8,....

def fibonacciSeries(n):
    fib = []
    sum = 0
    for index, value in enumerate(range(0,n+1)):
        if(index == 0):
            fib.append(0)
        elif(index == 1):
            fib.append(1)
        else:
            fib.append(fib[index - 1] + fib[index - 2])
        sum += fib[index]
    return fib, fib[n], sum

print(fibonacciSeries(15))