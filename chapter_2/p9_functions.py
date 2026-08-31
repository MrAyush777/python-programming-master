# function definition :

def avg():
    a = int(input('enter your number : '))
    b = int(input('enter your number : '))
    c = int(input('enter your number : '))
    
    average = (a+b+c) / 3
    # print(average)
    return average
a = avg() # here we called function. it says that here it will executed
print(a)
avg() # function call

print("\n----------  ----------\n")

# def gd(name): # here name is parameter
#     print("good day, ",name)
# gd('ayush') # calling funtion with paraamtere value
# gd("mahi")


# def ayush(name,ending):
#     print(f'my name is {name}...')
#     print(f'hello bros...its {ending}')
#     return 999 #return name,ending

# a = ayush('ayush','2pm')
# print(a)