# in python, we can pass a function as argument of another function

def add(num1):
    return num1 + 10

def square(num2):
    return num2 ** 2

print(add(10))
print(square(5))

n = int(input("enter a number : "))
res1 = add(n)
res2 = square(res1)

print(res1,res2)