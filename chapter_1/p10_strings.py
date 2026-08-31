# strings are immutable (means we can not change the value of the strings) it's not possible

a = 'ayush' # single quoted string
b = "ayush" # double quoted string
c = '''ayush''' # triple quoted string
print(a)
print(b)
print(c)


#  in python strings are immuatable, it means we can not change an existing string

# if you want to print some part of the string than write like below : : 
# it's called string slicing: 

nameShort = a[0:3]
print(nameShort," 1") # ayu

# if you want to print only one character from the string than write like below :
print(nameShort[1:]," 2") # is same as print(nameShort[1:5])
print(nameShort[2]," 3") # is same as print(nameShort[0:4])
print(nameShort[1:5]," 4") 

# we can provide a skip value as a part of our slice like this :

word = "amazing"
ans = word[1:6:2] # mazing # 
# mazin # mzn
print(ans)  # mzn
# to solve this code first solve '1:6' and than solve 'result:2'