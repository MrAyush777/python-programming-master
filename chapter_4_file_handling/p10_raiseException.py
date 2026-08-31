# Raise an exception program :
# here we are going to raise an exception when the user enter the negative salary value. we can raise an exception by using 'raise' keyword and then we have to specify the type of exception that we want to raise and also we can write the message that we want to show when the exception is raised. 

salary = int(input("Enter your salary : "))

if salary < 0:
    raise ValueError("Salary cannot be negative...")
else:
    print("your salary is",salary)

