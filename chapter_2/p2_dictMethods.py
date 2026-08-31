# DICTIONARY METHODS :

marks = {
    "haryy" : 100,
    "ayush" : 23,
    "rohan" : 56,
    "mk" : [1,2,3]
}

# we can add a new key value pair in dictionary like this :
marks["krunal"] = 69
print(marks)

# we can also change the value of existing key like this :
marks["harry"] = 85
print(marks)


#1 items method
print(marks.items())
# if you want to retrieve particular row and|column than write like this:
print(list(marks.items())[1][0])
print(list(marks.items())[1][1])


#2 keys method
print(marks.keys())


#3 values of associated keys(value) method
print(marks.values())


#4 update method || update value of key
marks.update({"ayush" : 99})
print(marks["ayush"])
print(marks)
# we also can write like this to update value of key :\
marks["ayush"] = 45 
# or :
upadated_pair = {"ayush" : 77}
marks.updated(upadated_pair)


# important about dictionary : below it also ad a new pair which was not in dictionary... it is mutable...
marks.update({"ayush":10, "mehul":20})
print(marks)


#5 get method : returns the values of the specified keys
print(marks.get("mehul")) # returns value of that key
print(marks["mehul"]) # returns value of that key
print(marks.get("abcdefg"))  # it will return 'None'
# if the key is not present than it will return None. but i want to print a custom message if key is not present than do like this:
print(marks.get("xyz","this key is not present in dictionary"))

# what is we get the value that not exist(key not exist) lets check
print(marks.get("mehul00")) # it returns None wile
# print(marks["mehul00"]) # it returns an error 'Traceback()'


#6 clear() method
op ={
    1:"abc",
    2:"def"
} 
print(op)
op.clear()
print(op)


#7 copy()b method
cpy = {
    "name":"ayush",
    "age":20,
    "gender":"male" 
}
print(cpy)
details = cpy.copy()
print(details)


#8 pop() method : removes and retrieves the value linked with a given key from a dictionary.
a = {
    'name' : 'ayush',
    'age' : 20,
    'country' : 'india'
}
print(a)
a.pop('age')
print(a)


#9 popitem() is used to remove and return the last inserted key-value pair as a tuple. if the dictionary is empty then it raises a keyError.
print(a)
print(a.popitem())


#10 fromkeys() method : it gets keys and make values none for all keys
b = {
    10 : 'abc',
    20 : 'def',
    30 : 'ghi'
}
c = (10,20,30,40,'abc')
e = b.fromkeys(c)
print(e)

# there can't be duplicate keys in dictionary but values can be duplicate.
# keys can not be mutable data types like list.
# values can be mutable data types like list.

