# # BREAK     CONTINUE    PASS    statements

# # 1) break statement : is used to come out ot the loop when encountered. i instructs the program to exit the loop now.

# for i in range(1,100):
#     if(i==50):
#         break # it will exit the loop when the value is = 50 | not print 50(last value)
#     print(i)
    
# # 2) continue statement : it will skip the iteration if condition is true. and next iterate from start

# for i in range(1,100):
#     if(i==50):
#         continue # it will skip the curremt iteration of the loop when the value is = 50 | not print 50 and than continue to the next one
#     print(i)

# # 3) pass statement : pass is a null statement in a python. it instructs to do nothing. without pass statement the progam will throw an error. 

# for i in range(100):
#     pass #  is used when we dont want to perform anything in the loop but we also want that the error will not throw. so we just write pass statement. and it performs nothing. 

# # --------------------------------------- practice set ---------------------------------------------#

# print('\n-----------------------------------\n') 

# # 1) write a program to print multiplication table of given number using for loop.

# n = int(input('enter number for mul table : '))
# for i in range(1,11):
#     print(f'{n} X {i} = {n*i}')
    
# print('\n-----------------------------------\n') 

# # 2) write a program to create all the person names stored in a list 'l' which starts with 's'

# l = ['ayush','harry','mahi','kamo','kohinoor','krish']
# for name in l:
#     if(name.startswith('k')):
#         print(f'hello {name}') 
        
# print('\n-----------------------------------\n') 

# # 3) solve Q-1 using while loop.

# i=1
# mul = int(input('enter the number : '))
# while(i<=10):
#     print(f'{mul} X {i} = {mul*i}')
#     i+=1
   
# print('\n-----------------------------------\n')    

# # 4) write a programe to find whether a given number is prime of not ?

# n = int(input('enter num to find prime : '))
# for i in range(2,n):
#     if(n%i==0):
#         print('number is not prime')
#         print(i)
#         break
    
# else:
#     print('number is prime')
#     print(i)
    
# print('\n-----------------------------------\n') 

# # 5) write a programe to find out some of first n natural numbers using while loop

# n = int(input('enter number : '))
# i = 1
# sum = 0
# while(i<=n):
#     sum = sum + i
#     i+=1
# print(sum)

# print('\n-----------------------------------\n') 

# # 6) write a program to find the factorial of a given number using for loop

# x = int(input('enter Fact Num : '))
# fact = 1
# for i in range(1,x+1):
#     fact*=i
#     # i+=1
# print(f'the factorial of {x} is {fact}')

# ''' 7)  write a program to print the following * patterni
#   *
#  ***


# ''' FOR SOLVE AND LOGIC FOR THIS PROGRAM SEE THE CODE WITH HARRY : PYTHON COURCE : TIME : 4:35:45

# n = int(input('enter number : '))
# for i in range(1,n+1):
#     print(' ' * (n-i),end='')
#     print('*' * (2*i-1),end='')  
#     print('')

''' 8) write a program to print  a following pattern :
*
**
***     for n = 3                                   ''' 

# n = int(input('enter number : '))
# for i in range(1,n+1):
#     print('*' * i,end='')  
#     print('')


''' 9) write a program to print  a following pattern :
***
* *
***     for n = 3                                   ''' 

# t = int(input('enter the number : '))
 
# for i in range(1,t+1):
#     if(i==1 or i==t):
#         print("*" * t,end='')
#     else:
#         print("*",end='')
#         print(" " * (t-2),end='')
#         print("*",end='')
#     print("") 
    
# 10) write a program to print a multiplication table using for loop in reverse order.
# for logic you can see time : 4:48:00
g = int(input('enter num for mul reverse table : '))
for i in range(1,11):
    print(f"{g} X {11-i} = {g*(11-i)}")