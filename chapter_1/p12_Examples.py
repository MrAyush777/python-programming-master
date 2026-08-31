#`1st program 11111111111111111111 ` write a python program to display a user entered name followed by good afternoon using input() function.

print("enter your name : \n")
name = input()

print("Good Afternoon ! ",name) # normal method 

print(f"good afternoon ! {name}") # new method after new version released, here we used fstring to use existing variable inside the string, itw new and very easy and helpful method. take the syntax of this method in mind. here we write 'f' alphabet before the starting of the string and used curly braces where we need to use the varible.

print("good afternoon ! "+ name ) # it is an old method 


# 2nd program 222222222222222222222 write a program to fill in a letter template given with name and date.


letter = ''' Dear <|Name|>,
you are selected
<|Date|>
'''
print(letter)
print(letter.replace("<|Name|>","Ayush").replace("<|Date|>","14 Augast 2025"))
print(letter)


# 3rd program 33333333333333333333  write a programme to detect double space in a string.

stri = "ayush is  a good  boy" 
print(stri.find("  "))
# it return the number of index where it finds the word we entered in the fine() method
# it returns '-1' if the word is not found  


# 4th program 444444444444444444444 replace the double space from problem 3 with single spaces.

print(stri.replace("  "," "))