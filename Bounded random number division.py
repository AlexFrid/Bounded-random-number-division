import numpy as np


def divide_Number(n, t):
    '''
    Allows you to specify 2 numbers:
    1. The number you want divided
    2. The number you want it divided by
    The function then divides the number randomly
    into the specificed segments,with the condition
    that the sum of all the divided segments need to
    add up to the original number.
    '''
    nt = np.repeat(n, t)
    p = np.round(np.random.random(size=t), 1)
    while sum(p) != 1:
        p = np.round(np.random.random(size=t), 1)
    y = nt * p
    return y


test = divide_Number(17, 5)

print(test)
print(sum(test))
