import json

# print(students, type(students))
'''
with open("p11studentData.json",'w') as fs:
    json.dump(students,fs,indent=3)
'''

# load() : this method is used to read the json file and convert it into python object, so we can use it to read the json file and convert it into python object and then we can use it in our program.

'''
with open("p11studentData.json",'r') as fs:
    data = json.load(fs)
print(data)
print(type(data))
'''

# update() : 

# follow below steps to update the json file :

# step 1 : read the old data from the json file and convert it into python object.
with open("p11studentData.json",'r') as fs:
    data = json.load(fs)


# step 2 : update the data that we want to update in the python object.
data.update(students)   


# step 3 : write the updated data back to the json file. (through dump() method)
with open("p11studentData.json","w") as fs:
    json.dump(data,fs,indent=3)



# you can also write exception like : fileNotFoundError, if file doesnt exist that how it can be update ? so create it and write data into it. use excepte block to write these things.




