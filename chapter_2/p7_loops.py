# 1) for loop

print('\n------------- for loop')
for i in range(1,10): # it will print 1 to 9 numbers
    print(i)
    
for i in range(10): # it will get automatically 
    print(i)
    
# range function : it generates an immutable sequence of numbers. it is commonly used in for loops to iterate a specific number of times or over a sequence of indices. the range function can be called with one, two, or three arguments.

for i in range(0,101,2):
    print(i)

# to print all elements of list we can use above syntax :
l = [1,1.45,'ayush',333]
for i in l:
    print(i)
    
# to print all elements of tuple we can use above syntax :
t = (1,3,1.23,'ayush',True )
for j in t:
    print(j)
    
# to print string using for loop we can use above syntax :

s = 'iAmAyushHowAreYous'
for k in s:
    print(k)
    
# for loop with else : 

l = [1,1.45,'ayush',333]
for i in l:
    print(i)
else:
    print('go fuck yourself') # this will executed when the loop exhausts(exit)

# 2) while loop

j = 11
while(j<=20):
    print(j)
    j+=1 # j = j + 1
    
print('------------- 2\'nd while loop')

# create a while loop that print elements of list

k = [12,34,45,56,67]
i = 0
while(i<len(k)):
    print(k[i])
    i+=1

