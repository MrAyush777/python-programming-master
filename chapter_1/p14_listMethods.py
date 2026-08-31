friends = ["Apple", "Orange", 5, 344.54, False, "Askash", "Rohan"]
print(friends)

# insert method is used to insert value/element inside list
# in insert method , here at first argument the index is written where the element is going insert. and second argument is value itself. 
nums = [1,34,62,2,6,11]
nums.insert(2,25) 
print(nums)

# but difference between append and extend is that append can add only one element at the end of the list at a time while extend can add multiple elements at the end of list at a time.
# append method of list add the element/value at the end of the list
friends.append("Mahi")
print(friends)

# sort method of list sort all numbers from the list and returns sorted values when access/print
# by default sort method sort the values in ascending order, to sort in descending order we have to pass 'reverse = True' inside sort method

nums.sort()
print(nums)

# to sort in descending order
nums.sort(reverse=True)

# reverse method of list reverse the elements/values of list 
# EX 1:
nums = [1,34,62,2,6,11,1,25,1,200,1]
nums.reverse() 
print(nums) # 11 6 2 62 34 1

# count() : it returns the count of given element in the list
print(f"the 1 appears {nums.count(1)} times in the list")

# EX 2:
days_of_week = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
print(days_of_week)
days_of_week.reverse()
print(days_of_week)

# print(nums.pop(6)) it will return the element that is going to delete/pop
# pop() method will delete element at given index and return its value.
nums.pop(6) #it will delete the element at the 6th index.
print(nums)
# if we don't provide any index inside pop() method, by default it will delete the last element of the list.

# it will remeove 34 from the list, here 34 is element not the index 
nums.remove(34)
print(nums)

# min() method will return the minimum value from the list
print(f"the minimun number of the list is {min(nums)}")

# max() method will return the maximum value from the list
print(f"the maximum number of the lists is {max(nums)}")

# sum() method will return the sum of all numbers from the list
print(f"the sum of all numbers from the list is {sum(nums)}")

# in : the membership operator
# it checks whether the given element is present inside the list or not, if present then return True otherwise False
print(200 in nums)
print(2 not in nums)

# NESTED LISTS : A LIST INSIDE ANOTHER LIST
LT1 = [1, 20.3, False, "hello", ["A","B","C"]]
print("list inside another list : ",LT1)
print(LT1[4],LT1[-1])
print(len(LT1))
print(LT1[-1][1] ) # it will access the B from the nested list

LT2 = [ [1,2],[3,4],[5,6],[7,8,[9,10]]]
print(f"the length of the LT2 is {len(LT2)}") # it will return 4 because there are 4 elements in the LT2 list, 4th element is also a list
print(f"TO RETREIEVE 9 FROM THE INNERMOST LIST, WRITE LIKE THIS : {LT2[-1][-1][0]}")

# ----------------------------------------------------------------------------------------------------------

fruits = ["apple", "banana","grapes","orange","kiwi"]
print(fruits.append("mango"))
print(fruits)

print(fruits.insert(2,"orange"))
print(fruits)

fruits.extend(["omega","papaya"])
print(fruits)

fruits.remove("grapes")
print(fruits)

fruits.pop(1)
print(fruits)

# if you want to change the value at particular index of list, you can do it like this :
fruits[3] = "blueberry"
print(fruits)

scores = [2,45,102,4,9,12,45,90,1,1]
total = 0
for score in scores:
    total += score # total of scores.
print(f"the total score of is : {total}")

# sum() function
print(f"the total score is {sum(scores)}")


# find highest score using for loop : 
highest = scores[0]
for score in scores:
    if(highest < score):
        highest = score
print(highest)

# find highest/maximum score using max() function
print(f"the maximum/highest score is {max(scores)}")

# find lowest/minimum score using min() function
print(f"the minimum/lowest score is {min(scores)}")