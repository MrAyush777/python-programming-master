"""
we have the following dictionary containing details :

user = {
    "name" : "john",
    "password" : "1234",
    "email" : "abc@gmail.com"
    address : "noida"
    country : "india"
}

delete the sensitive information from the from the dictionary present in a list : 
sensitive_info = ['password', 'address']

"""
user = {
    "name" : "john",
    "password" : "1234",
    "email" : "abc@gmail.com",
    "address" : "noida",
    "country" : "india"
}

sensitive_info = ['password', 'address','phoneNo']

# method 1 : this method is not working because we are changing the dictionary while iterating it. so we will get error : RuntimeError: dictionary changed size during iteration
# for info in user:
#     if info in sensitive_info:
#         user.pop(info)


# method 2 : this method is working because we are iterating the list and not the dictionary. so we are not changing the dictionary while iterating it. so we will not get error : RuntimeError: dictionary changed size during iteration

# for i in sensitive_info:
#     user.pop(i)
# print(user)



# printing key and value of the dictionary : 

# for i in sensitive_info:
#     print(f"key : {i} , value : {user[i]}")
#     user.pop(i)

# print(user)

for i in sensitive_info:
    if i in user:
        print(f"key :{i},value : {user[i]}")
        user.pop(i)
    else:
        print(f"{i} is not present in dictionary..")
print(user)

