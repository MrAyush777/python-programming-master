# check the type of variable assigned using input () function.

a = input("enter any value to ")
print("the type of variable a is : ",type(a))


# use comparison operator to find out where a given variable 'a' is greater than 'b' or not. take 'a = 34' and 'b =80'

a = int(input("enter number 1 : "))
b = int(input("enter number 2 : "))

print("a is greater than b is : ",a>b)


# write a python program to find an average of two numbers entered by the user.

print ("it is an averager calculator : ")
a = int(input("enter no 1 : "))
b = int(input("enter no 2 : "))

print("the average of both numbers is : ",(a+b)/2)


# write a python program to calculate the square of a number entered by the user  : :
print("power calculator : ")
a = int(input("enter the number : "))
print("the square of a is : ",(a*a))


# and if you want to power any integer than write like below :

print("the square of a is : ",(a**2)) # it will print square of a
print("the square of a is : ",(a**3)) # it will print 3 power of a, means a*a*a