# 1) write a program to create a dictionary of hindi words with values as their english translation. provide user with an option to look it up.
words = {
    "madad" : "help",
    "khursi" : "chair",
    "biladi" : "cat"
}

word = input("enter the word you want meaning of : ")

print(words[word])

# --------------------------------------------

# 2) write a program to input 8 numbers from the user and display all the unique numbers(once) usig set.

x = set()

n = input("enter number : ")
x.add(int(n))
n = input("enter number : ")
x.add(int(n))
n = input("enter number : ")
x.add(int(n))
n = input("enter number : ")
x.add(int(n))
n = input("enter number : ")
x.add(int(n))
n = input("enter number : ")
x.add(int(n))
n = input("enter number : ")
x.add(int(n))
n = input("enter number : ")
x.add(int(n))

print(x)

#___________________________________________________

# 3) can we have a set with 18 as (int) and '18' as (str)   as a value in it ?  || yes

y = set()
y.add(18)
y.add('18')
print(y)

# 4) what will be the length of following set : 
z = set()
z.add(20)
z.add(20.0)
z.add('20')
print(z,len(z)) # output will be 2 | it ignores datatypes when compare 20 and 20.0. both are same numerically.

# 5) what is a type of  b  below ? :

b = {}
print(type(b))

# 6) create an empty dictionary. allow 4 friends to enter their favourite language as value and use key as their names. assume that the names are unique.

v = {}
name = input('enter friend name : ')
lang = input('enter language name : ')
v.update({name : lang})

name = input('enter friend name : ')
lang = input('enter language name : ')
v.update({name : lang})

name = input('enter friend name : ')
lang = input('enter language name : ')
v.update({name : lang})

name = input('enter friend name : ')
lang = input('enter language name : ')
v.update({name : lang})

print(v)

# 7) if the names of two friends are same , what will happen  to the program in problem no 6 ?
# --> the last input will be saved

# 8) can you change the values inside a list which is contained in set g ?

g = {8,7,12,"haryy",[1,2]}
# g[4][0] = 9
# it will throw an error like below :
# TypeError: unhashable type: 'list'

# reason : you cannot change the value inside a list contained in a set. in fact, you cannot even have a list as an element in a set because sets in python requier all their elements to be immutable and hashable. lists are mutable and not hashable. so they cannot be added to set