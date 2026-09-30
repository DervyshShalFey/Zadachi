from math import *
from transformation import *

try:
    x = float(input('Insert number: '))
    x = transform(x)
    y = float(input('Insert 2nd number: '))
    y = transform(y)
    z = float(input('Insert 2nd number: '))
    z = transform(y)
    print(f'A) -1 / {x}^2 = {transform(-1/x**2)}')
    print(f'Б)')
except ValueError:
    print('Not a number!')