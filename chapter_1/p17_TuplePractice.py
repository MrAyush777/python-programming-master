# 1 ==== write a program to store seven fruits in a list entered by the user.

# fruits = []

# f1 = input("enter fruit name 1 : ")
# fruits.append(f1)

# f2 = input("enter fruit name 2 : ")
# fruits.append(f2)

# f3 = input("enter fruit name 3 : ")
# fruits.append(f3)

# f4 = input("enter fruit name 4 : ")
# fruits.append(f4)

# f5 = input("enter fruit name 5 : ")
# fruits.append(f5)

# f6 = input("enter fruit name 6 : ")
# fruits.append(f6)

# f7 = input("enter fruit name 8 : ")
# fruits.append(f7)

# print(fruits)


# # 2 ==== write a program to accept marks of 6 students and display them in a sorted menor


# Marks = []

# m1 = int(input("enter marks here 1 "))
# Marks.append(m1)

# m2 = int(input("enter marks here 2 "))
# Marks.append(m2)

# m3 = int(input("enter marks here 3 "))
# Marks.append(m3)

# m4 = int(input("enter marks here 4 "))
# Marks.append(m4)

# m5 = int(input("enter marks here 5 "))
# Marks.append(m5)

# m6 = int(input("enter marks here 6 "))
# Marks.append(m6)

# print(Marks)
# Marks.sort()
# print(Marks)

# # 3 ==== check that the tuple type cannot be changed in python...

# '''a = (34,44,"ayush")
# a[2] = "abc" '''

# # 4 === write a program to sum a list of 4 numbers

# l=[2,55,86,91]
# print(sum(l))

# # 5 === write a progrm to count the number of 0's in the following tuple

# a=(9,0,0,3.4,1,0,5,7,0)
# n=a.count(0)
# print(n)

ab_1 = ("i am ayush ","i am ironman ")
ab_2 = (10,20,30,40,20,30,20,40,50)

abc = ab_1 + ab_2
print(abc)

print(ab_1 * 4)
print(20 in ab_2)

print(ab_2.count(20))

print(ab_2.index(20,5))

print(min(ab_2))
print(max(ab_2))
print(sum(ab_2))

s1 = "i am iron man"
s2 = s1.replace("am","was")
print(s2)

# id method is used to get the address of the variable in the memory 

_s1 = id(s1)
_s2 = id(s2)
print(_s1,_s2)

x = (1,2,3,4,5)
# x.append(6)  # This will raise an AttributeError because tuples are immutable
# print(x)

x[-1 ] = 6
# print(x) # This will also raise a TypeError because tuples do not support item assignment
