# range() : built-in function used to generate sequence of integers in a given integers.
# syntax : range(start,stop,step) - stop is not included 
# other syntax : rnage(start,stop) - step=1 by default here.
# range(stop) : => 0 to stop-1 with step of 1, start = 0 by default. 

# ex 1 :
for i in range(5):
    print(i) # it will print 0 to 4
    

# ex 2 : other important method ...
groceries = ['salt','sugar','chilli-powder']
for i in groceries:
    print(i)
    # second mehtod : 
for i in range(len(groceries)):
    print(i)
    
# ex 3 : 
profits = [9,11,6,10]
for index in range(len(profits)):
    quarter = index+1
    # print(quarter,profits[index])
    print(f"profit for quarter {quarter} is {profits[index]}")