# _________________________________ TUPLE _______________________________________________

# tuples are coma separated values enclosed within parenthesis(). sequence of items as a collection 
# a tuple can hold values that have different data types
# we can't make changes in existing tuple. elements are fixed. 

a = (1,2,3,4) # it a way to write tuple
b = () # we can also make an empty tuple, it is allowed
c = (1) # but if you write like this , than python will understan like we enter number inside bracket, not see as a tuple datatype . it consider it as a integer value.

print(type(a))
print(type(b))
print(type(c)) # here we can see that python interpreter consider it as a interger datatype not a tuple

# well if you want to make a tuple that consist only one element than write like below :
d = (1,) # it is a right way to make a tuple with one element, here we put coma(,) just after element
print(type(d))

print(a)
print(b)
print(c)
print(d)

t1 = (1,"hello",3.40,False, True,[10,20.20,True],(1,2,34))
print(t1)
print("the length of the given tuple t1 is : ",len(t1))
print(t1[4])
for t in t1:
    print(t)

# here t2 is also a tuple even we don't use parenthesis(). round bracket is ooptional while creating a tuple.
t2 = 10,20,30
print(t2,type(t2))

# we can also use tuple() constructor to create a tuple
t3 = tuple((100,200,300,"hi"))
print(t3,type(t3))

# we can perform type casting in tuple also
l1 = [1,2,3]
print(l1,type(l1))
t4 = tuple(l1)
print(t4,type(t4))
# works same when casting from tuple to list