s = {1,3,45,56,5,"ayush",5,2}
print(s,type(s))

# METHODS OF SET : : : 

# 1) add() : add element in the set | it takes only one argument
s.add(444)
print(s)

# 2) len() : returens length of a set
print(len(s))

# 3) remove() : used to remove element from the set and it also update
s.remove(5)
print(s)

# 4) discard() : it also removes the element from the set but if the element is not present in the set it will not give error
s.discard(1000) # no error will be shown
# 4) pop() : it will remove(delete) a random element from the set
s.pop()
print(s)

# 5) clear() : it will clear all elements from the set 
s.clear()
print(s)


# : : : UNION AND INTERSECTION  : : :

# 6) union(set1,set2) : returns a new set with all items from both sets
s1 = {1,45,8,6}
s2 = {7,8,1,78}
print(s1.union(s2))
# it's alternative is '|' operator :
print(s1 | s2)


# 7) intersection(set1, set2) : return a set which contains item which are in both sets.
print(s1.intersection(s2))
# it's alternative is '&' operator :
print(s1 & s2)

# 8) difference(set1,set2) : returns a set which contains items which are in set1 but not in set2
print(s1.difference(s2))
# it's alternative is '-' operator :
print(s1 - s2)

# --------------------------------------
# THERE ARE MANY SET METHODS LILKE :
# issubset(), issuperset(), difference()

# if no value is matched in union/intersection/difference method it will return empty set {} : set()