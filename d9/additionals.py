import numpy as np

# argumenty i kwargs
def function_2(x, y):
    return int(x * y)


# wywolanie funkcji argumenty sa tuple, a key word argumenty sa dictem
def function(first_argument, *args, **kwargs):
    print('First required argument: {}'.format(first_argument))
    print('Args: {}'.format(args))
    print('Kwargs: {}'.format(kwargs))
    if kwargs.get('print_this'):
        print('Printing value of print_this argument: {}'.format(kwargs.get('print_this')))
    else:
        print('No print_this kwarg provided')
    step = function_2(args[1], 1)
    new_step = kwargs.get('new_step')
    if new_step:
        step = new_step
    return np.arange(first_argument, args[0], step)


print(function(10, 101, 3, 'unused', keywordarg='anything', print_this='Hello', new_step=10))

arguments = [21, 10, 10, 10, 10]
kwarguments = {'new_step': 1, 'next': 'WOW'}

print(function(*arguments, **kwarguments))


# liczenie czasu wywolania funkcji
def asd():
    return np.arange(10, 100000)


def time_calculate_decorator(function):
    import time
    start = time.time()
    result = function()
    print(time.time()-start)
    return result + 1


print(time_calculate_decorator(asd))