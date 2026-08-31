# 1) filter : the filter function is used to filte out the element from the list based on the condition provided by the user.
# it takes two arguments, the first one is the function and the second one is the iterable(sequence).

# syntax : 
# filter(function,sequence)

seq = [1,2,3,4,5,6,7,8,9]
odd = lambda x : True if x%2 != 0 else False
output = filter(odd,seq)
print(list(output)) # here we will get the filter object which is an iterator, to get the list we need to convert it into list.

# 2) map : the map function is used to apply a function to all the elements of the iterable(sequence) and return a map object which is an iterator.

seq2 = [1,2,3,4,5]
map_output_1 = map(lambda x : True if x%2 != 0 else False,seq2)
map_output_2 = map(lambda x : x ** 2,seq2)

print(list(map_output_1))
print(list(map_output_2))