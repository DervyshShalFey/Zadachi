from math import *
from transformation import *

try:
    x = float(input('Insert 1st number: '))
    x = transform(x)
    y = float(input('Insert 2nd number: '))
    y = transform(y)
    z = float(input('Insert 3rd number: '))
    z = transform(z)
    try:
        print(f'A) {x}/{neg(y)}/{neg(z)} = {transform(x/y/z)}')
    except:
         print('A) Can\'t divide by zero!')
    try:
        print(f'Б) {x}*{neg(y)}/{neg(z)} = {transform(x*y/z)}')
    except:
        print('Б) Can\'t divide by zero!')
    try:
        print(f'B) {x}/{neg(y)}*{neg(z)} = {transform(x/(y*z))}')
    except:
        print('B) Can\'t divide by zero!')
    try:
        print(f'Г) ({x}{pluey(y)})/{neg(z)} = {transform((x+y)/z)}')
    except:
        print('Г) Can\'t divide by zero!')
    try:
        print(f'Д) {x}+({y}/{neg(z)}) = {transform(x+(y/z))}')
    except:
        print('Д) Can\'t divide by zero!')
    try:
        print(f'E) ({x}{pluey(y)})/({y}{pluey(z)}) = {transform((x+y)/(y+z))}')
    except:
        print('E) Can\'t divide by zero!')
    try:
        print(f'З) {x}/sinus of {y} = {x/sin(y)}')
    except:
        print('З) Can\'t divide by zero!')
    try:
        print(f'И) 1/(2*{neg(x)}*{neg(y)}*sinus of {z}) = {1/(2*x*y*sin(z))}')
    except:
         print('И) Can\'t divide by zero!')
    try:
        print(f'K) (2*{neg(y)}*{neg(z)}*cosinus of {x}/2)/({y}{pluey(z)}) = {(2*y*z*cos(x/2))/(y+z)}')
    except:
         print('K) Can\'t divide by zero!')
        
        
except ValueError:
    print('Not a number!')