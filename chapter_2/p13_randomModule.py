import random
# it generates random floting point numbers between 0 and 1

# it will generate different random numbers every time you run the program because it is based on the current system time.
# print(random.random())

# randint(a,b) --> it prints random number between a and b. here a dnd b can any integer.
# print(random.randint(1,100))

l1 = [1,45,666,78,122]
# print(random.choice(l1))
print(l1)
# shuffle() : this function is used to randomly rearrange the elements of a list. 
# it does not return any value but it changes the original list.
# it modifies the original list.
# it only works with mutable sequences like list.
print(random.shuffle(l1)) # it will return None because it does not return any value but it changes the original list.
print(l1)

# with strings : if we want to shuffle the characters of a string then we can convert the string into a list and then shuffle the list and then convert it back to string.
# directly we cannot shuffle the string because string is immutable in python. we cannot change the original string but we can create a new string with shuffled characters.
s = "hello"
l = list(s)
print(random.shuffle(l))
print(l)

