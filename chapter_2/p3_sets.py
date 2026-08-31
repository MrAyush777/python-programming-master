# sets are collection of unique items only , unordered and unindexed and non-sequential.
# in sets the items are coma separated and enclosed within curly braces {}
# sets do not allow duplicate values , it only store unique values.
# sets are mutable , we can add or remove items after set creation.
# concatenation and replication are not possible in sets.
# sets can be overwritten but not indexed. we can typecast other data types to sets. like list , tuple , dictionary etc. to set.


# # declaration of set :


# s = {1,2,3,3,3,3,4,4,5,5,5,5,5,5,5}
# print(type(s))
# print(s) # it will print only unique items only one type , not repeat twice.

# # below is a wrong method of define empty set | it will return the type = dictionary
# t = {}
# print(type(t))

# # the correct method is given below to define empty set :
# e = set()
# print(type(e))


set = {"a","b","c"}
print(set)

set3 = {101,"ayush",20,True,False}
print(set3,type(set3),len(set3))

for item in set3:
    print(item)

weekdays = {"mon","tue","wed","thu","fri"}
# weekdays_set = set(weekdays)
print(weekdays)

weekdays.discard("abc")
print(weekdays)

# weekdays.remove("cde") # it wil give error if the item is not present in the set
print(weekdays)


# --------------------------------------- FROZEN SETS : ---------------------------------------
# frozen sets are immutable sets , we cannot add or remove items from frozen sets after its creation.
# frozensets are hashable and can be used as keys for dictionaries or elements of other
# but we can perform union, intersection and difference operations on frozensets.
fr_set1 = frozenset({1,2,3,4,4,5})
print(fr_set1,type(fr_set1))