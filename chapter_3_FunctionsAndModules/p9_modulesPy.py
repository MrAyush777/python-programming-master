# modules : .py file is a module. .py file can contain functions, variables, classes, etc. we can import a module in another module or in the main program. we can use the functions, variables, classes, etc. of the imported module in the main program.
# there are two types of modules in python : 1. built-in modules 2. user-defined modules

# 1) built-in modules : these are the modules that are already available in python. we can import these modules and use their functions, variables, classes, etc. in our program. some of the built-in modules are : math, random, datetime, os, sys, etc.

# how to import a module : 
# syntax : import module_name

import math
# instead importing the whole module we can import specific functions, variables, classes, etc. from the module using the following syntax :

from random import randint

# calculate square root of a number
n = 100
sroot = math.sqrt(n)
print(f'the square root of {n} is {sroot}') 

# calculate area of circle
radius = 5
area = math.pi * (radius ** 2) # here pi is a constant in math module
print(f'the area of circle with radius {radius} is {area}')
print(math.pi) 

# generate a random number between 1 and 6
randomNum = randint(1,6) # do not write module name before the function name when we import specific functions from the module
print(f'the random number between 1 and 6 is {randomNum}')

# syntax to create an alias for a module that is imported : import module_name as alias_name
import datetime as dt

time = dt.time(8,45,40)
print(time)

print( 100 ** 0.5) # it will give the same result as math.sqrt(100) but it is not recommended to use this method to calculate square root of a number because it is not readable and it is not clear that we are calculating square root of a number. it is better to use math.sqrt() function to calculate square root of a number because it is more readable and it is clear that we are calculating square root of a number.

