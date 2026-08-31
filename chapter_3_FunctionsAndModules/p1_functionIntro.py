# syntax : 
# def functioin_name(pamameters):
    # statements here
    
def greet(name):
    print(f"hello i am {name}. Good morning...")

greet("ayush")
greet("ayush")

# ----------------------------------------------------------------------------------

def even_odd(num):
    if num % 2 == 0:
        print("even number...")
    else:
        print("odd number...")

even_odd(10)
even_odd(11)

# ----------------------------------------------------------------------------------

def add(a,b):
    print(a+b)

add(10,30)

# to see if function is returning something or not we can store it in variavle when we call the function like this :

result = add(10,30)
print(result) # it will print None because we are not returning anythin from the function add() we are just printing the sum of a and b but not returning it so wnen we try to store the result of add(10,30) in variable result it will store None because there is no return statement in the function add() so it will return None by default.
 
def add2(a,b):
    return a + b

result2 = add2(10,40)
print(result2)


# ----------------------------------------------------------
# function returnin multiple values.

def arithmetic(a,b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return add,sub,mul,div

a = int(input("enter first num : "))
b = int(input("enter second num : "))

w,x,y,z = arithmetic(a,b)
# print(v,x,y,z)
    
print(f"The addition of {a} and {b} is : {w}")
print(f"The subtraction of {a} and {b} is : {x}")
print(f"The multiplication of {a} and {b} is : {y}")
print(f"The division of {a} and {b} is : {z}")
    
