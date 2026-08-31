# lists can store multiple value with differen data types
# we can change the values of list just by assigning new value to it and also using index 
# IMP : lists are mutable (we can change values of existing list variable)
# we can access the value/values of list by using index
# also we can perform slicing

# friends = ["Apple", "Orange", 5, 344.54, False, "Askash", "Rohan"]

# print(friends)
# print(friends[0])

# friends[0] = "Ayush"
# print(friends[0])

# list slicing :

# print(friends[1:4])
# print(friends[3:7])

l1 = [3,8,1,0,4,9,7,3,6]
print(len(l1))
print(l1[1:6])
print(l1[1:6:1])
print(l1[2:7:2])


# concatenation of the list :
l2 = [1,7,2]
l3 = [0,5]
print(l2+l3)
print(l3+l2+l1)

# repetition of list :
print(l3 * 3)