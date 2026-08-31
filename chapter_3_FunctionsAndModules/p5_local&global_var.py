n = 1 # global variable : accessible throughout the program 
def fun():
    n = 20 # local variable : accessible only inside the function
    print('in' ,n)
fun()
print('out',n)

# now if i want to change the value of global variable n inside the function then i have to use global keyword
num = 50
def fun2():
    global num
    num = 30
    print(num)
fun2()
print(num)