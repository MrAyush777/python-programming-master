# the content of docstring is not important, but the format is important.
# docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. Such a docstring becomes the __doc__ special attribute of that object. The content of the docstring is used to document the object, and it can be accessed using the __doc__ attribute.
# Unlike standard comments (#), docstrings are stored as metadata and are accessible at runtime.
# Key Features :
# Placement: They must appear as the very first statement immediately after the definition of a function, class, or module.
# Syntax: They are typically enclosed in triple double quotes ("""...""") or triple single quotes ('''...'''), which allow them to span multiple lines.
# Access: You can view an object's docstring using the .__doc__ attribute or the built-in help() function.

def divide(num1,num2):
    """
    summary : 
    num1 : int : num to be divided (numerator)
    num2 : int : num that divided num1 (denominator)
    return float
    """
    result = num1 / num2
    return result

a = divide(20,5)
print(a)

print(help(divide))



def abc():
    """
    this is a docstring for abc function
    """
    print("this is abc function...")
    
print(help(abc))
print(divide.__doc__)