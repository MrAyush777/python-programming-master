def add(a,b):
    return a + b


# positional arguments : passing the arguments in order of their position 
print(add(10,20))

# default arguments : 
def add2(a,b=10):
    print(f"a : {a} , b : {b}") # here when we call the function add2() without passing the second argument it will take the default value of b which is 10 and it will print a : 10 , b : 10 but when we call the function add2(10,20) it will print a : 10 , b : 20 because we are passing the second argument as 20 so it will override the default value of b which is 10 and it will take the value of b as 20.
    return a + b

print(add2(10,20))
print(add2(10)) # here we are not passing the second argument so it wiill take the default value of b which is 10 and it will return 20

# there is one more aspect of default argument : the non-default argument should always be before the default argument in the function definition otherwise it will give an error because when we call the function add2(10) it will take the value of a as 10 and it will take the default value of b as 10 but if we define the function like this def add2(a=10,b) it will give an error because when we call the function add2(10) it will not know which argument is which because both arguments are default arguments so it will give an error. so we should always define the non-default argument before the default argument in the function definition.

# --> wrong way to define default argument :

# def add3(a,b=50,c):
#     print(f"a : {a}, b : {b}, c : {c}")
#     return a+b+c
# print(add3(10,20)) # here we are passing the value of a as 10 and the value of c as 20 but we are not passing the value of b so it will take the default value of b which is 50 but it will give an error because we have defined the default argument b after the non-default argument c so it will give an error because when we call the function add3(10,20) it will not know which argument is which because both arguments are default arguments so it will give an error. so we should always define the non-default argument before the default argument in the function definition.

# --> right way to define default argument :
def add3(a,c,b=50):
    print(f"a : {a},b : {b}, c : {c}")
    return a+b+c

print(add3(10,20))

# instead we also can write like this : 
# result = add3(10,20)
# print(result)

# keyword arguments : passing the arguments by their name
resultt = add3(10,c=50)
print(resultt)

# we can also change the order of the agruments like this :
print(add3(a=20,c=30,b=40)) # here order not matter because we are passing the arguments by their name so it will take the value of a as 20, c as 30 and b as 40 and it will return 90. so when we use keyword arguments we can change the order of the arguments because we are passing the arguments by their name so it will take the value of the argument based on its name and not based on its position.

# what is we not pass any argument ?
# print(add3())
# it will give an error : TypeError: add3() missing 2 required positional arguments: 'a' and 'c'

# what if we pass extra argument ?
# print(add3(10,20,30,40))
# it will give an error : TypeError: add3() takes from 2 to 3 positional arguments but 4 were given