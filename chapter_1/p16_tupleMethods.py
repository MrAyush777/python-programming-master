# count method (same as string method)

t =(4,3,6,4,4,7,9) 
print(t.count(4)) # output > 3, because 4 is comes 3 times in the tupls


# index method (same as string method)

d = (1,2,3,2,4,4,5,2)
print(d.index(2))
print(d.index(2,3))

# ___________________________________OPERATIONS OF TUPLE_____________________________________


# 1st operation slicing\
# you can access element from where you want by using slicing. just specify starting index , and the number of elements you want

print(d[2:6]) # (3,2,4,4)
print(d[4:8]) # (4,4,5,2)

# 2nd operation : length
# it returns the number of elements from the tuple

print(len(d))

# 3rd operation : membership test\
# it checks if the element exist in a tuple or not .

print(3 in d) # returns true if 3 found in tuple 'd' otherwise returns false
print(10 not in d) # returns true if 10 not found in the tuple 'd' otherwise returns false

# 4th operation : concatenation
# join two tuples together

t1 = (1,2)
t2 = (3,4,5)
print(t1 + t2) # here '+' operator concatenate both tuples and print it on terminal

# 5th operation : repetition
# repeat the tuple multiple times

print(t1 * 3) # it repeats the tuple 't1' three times and print it in terminal

#6th operation : iteration
# loop through the elements in a tuple
# it prints each element at the new line from the tuple we specify, here item is a temporary element that we used to print all elements of the tuple 'd' . item element holds the element of tuple 'd' , every time the loop iterate the value of 'item' element will be changed.
    
for item in d:
    print(item)


# 7th operation : tuple unpacking
# assign each element to a variable.
# tuples can be unpacked into individual variables. it means :

my_tuple = (1,2,3)
a,b,c = my_tuple
print(a,b,c)