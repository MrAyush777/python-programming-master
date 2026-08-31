# DICTIONARY SIMPLE EXAMPLE :

marks = {
    "haryy" : 100,
    "ayush" : 23,
    "rohan" : 56,
    "mk" : [1,2,3]
}

print(marks,type(marks))
print(marks['haryy'])
print(marks["mk"])

# to change the value of a particular key :
marks["rohan"] = 36
print(marks)

# print(marks["xyz"]) # it will give an error because this key is not present in dictionary

# membership operator in dictionary : 

print(100 in marks) # it will return False because it checks for key not value
print("haryy" in marks) # it will return True because it checks for key not value

# d = {[1,2,3 ]:6 , [4,5,6] : 15} # it will give an error because list is unhashable and we can not use list as key in dictionary
# print(d)
# keys cannot be list, set
# keys can be str,int, float, bool, tuple
# dictionary can not be key in dictionary but it can be value in dictionary.


d1 = {"nine" : 9,"five" : 5}
print(d1)
print(d1["nine"])

student1 = {'id' : 1, 'name' : 'ayush', 'marks' : {'eng' : 90, 'maths' : 95, 'history' : 85}}
print(student1)
print(student1['marks']['maths'])

print(student1.keys()) # it returns all the keys of dictionary
print(student1.values()) # it returns all the values from dictionary)
print(student1.items()) # it returns all the key value pairs in form of list of tuples