# 1 function with default parameter

def goodBye(name,ending='thank you'):
    print(f'good day my friend {name}...')
    print(ending)
goodBye('ayush') # calling function with default parameter
goodBye('ayush','thanks')

# 2 recursion : function calls itself

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

i = int(input('enter number for factorial : '))
print(f'the factorial of given number is {factorial(i)}')

# variable length positional argument(0 to n) : *args and **kwargs

def add(*args): # here args is a tuple that contains all the arguments passed to the function, and test "args" is a variable that can be used to access the arguments passed to the function. and variable name can be anything but we use "args" by convention.
    print(args,type(args))
    print(sum(args))
add()

def student(sid, sname, *marks):
    if len(marks) == 0:
        print(f"student {sname} with id {sid} has failed !")
    else:    
        percent = sum(marks) / len(marks)
        print(f"student {sname} with id {sid} has percentage {percent}%")
# here we use if...else condition. if the condition was not written then it will give error of "division by zero" because if the length of marks is zero then it will try to divide by zero which is not possible. so we use if...else condition to check if the length of marks is zero then we will print that the student has failed otherwise we will calculate the percentage and print it.

student(12,'Ayush',10,10,10)
student(10,'Mahi',10,10,10)
student(12,'Akshay') # here we are not passing any marks to the function so it will give error of "division by zero" because if the length of marks is zero then it will try to divide by zero which is not possible. so we use if...else condition to check if the length of marks is zero then we will print that the student has failed otherwise we will calculate the percentage and print it.




# **keyargs : variable length keyword arguments 
# the keyword arguments should be last arguments in the function definition because it will take all the remaining keyword arguments and store them in a dictionary. and we can access the values of the dictionary using the keys.
# it cannot be the first or middle argument because it will take all the remaining keyword arguments and store them in a dictionary. and we can access the values of the dictionary using the keys.
# if you want to use positional arguments and keyword arguments in the same function then you should use positional arguments first and then keyword arguments because if you use keyword arguments first then it will take all the remaining keyword arguments and store them in a dictionary. and we can access the values of the dictionary using the keys.
# still if you write positional arguments after keyword arguments then it will give error because it will take all the remaining keyword arguments and store them in a dictionary. and we can access the values of the dictionary using the keys.


def func(**kwargs):
    print(kwargs)

func() # it will print an empty dictionary because we are not passing any keyword arguments to the function.

func(x=10, y=20) # it will print a dictionary with keys x and y and their corresponding values 

def details(sid,sname,*activity, **marks):
    print(f"the {sname} with id {sid} has {marks} marks ")
    print(f"the {sname} has participated in {activity}")

details(11,'mahi','chess',maths=20,science = 40)
details(12,'ayush','cricket','football',maths=50, science=60)
details(13,'krish')


