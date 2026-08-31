import copy

l1 = [1,2,3,[4,5,6],'ayush']

# method 1 : using copy() method of list
l2 = l1.copy()
print(l2)

# method 2 : using copy  module of shallow copy
l3 = copy.copy(l1)
print(l3)
print(f"memory addresses :\n l1 : {id(l1)} , l2 : {id(l2)} , l3 : {id(l3)}  ")

l1[0] = 100
print(l1)
print(l3) # it will not change because it is shallow copy and it only copies the reference of the list not the actual list

a1 = [1,2,[3,4,5],"kunj"]

a1[1] = 100
a1[2][1] = 200
print(a1)

a2 = copy.deepcopy(a1)
print(a2)
# method 3 : using copy module of deep copy
