countries = ['India','Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'Estonia', 'Latvia', 'Lithuania', 'Russia', 'Poland']

# task 1 :  count all the countries whic ara starting with character 'i

# counter = 0
# for c in countries :
#     if c[0] == 'I':  # if c.startswith('L) :   
#         counter = counter + 1
# print(counter)


# task 2 : create a list of all the countries which are starting with character 'i' 

empty = []
for c in countries : 
    if c.startswith('I'):
        empty.append(c)

print(empty)