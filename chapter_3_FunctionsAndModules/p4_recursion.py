# recursion is a process in which a function calls itself till the certain condition not met    
# there are two parts of recursive function :
# 1) Base/terminating condition : it is the condition which will stop the recursive function to call itself 
# 2) Recursive condition : 

# 1) factorial using function and condition :
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * fact(n-1)
    
# print(fact(4))

# 2) factorial using while loop :
def fact2(num):
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1
    return factorial

ab = int(input("enter a number : "))
print(f"factorial of {ab} is {fact2(ab)}")