import pickle

students = {
    "student1" : {'name' : 'Ayush', 'age' : 20, 'percentage' : 90, 'sports' : False},
    "student2" : {'name' : 'Mahi', 'age' : 25, 'percentage' : 80, 'sports' : True},
    "student3" : {'name' : 'Roshni', 'age' : 22, 'percentage' : 100, 'sports' : False    },
}

print(students, type(students))

# serialization : this is the process of converting a python object into a byte stream, so that we can save it to a file or send it over a network. we can use pickle module to do this.

with open("p12_students.bin","bw") as fs:
    for student in students:
        pickle.dump(students[student],fs)

# deserialization : this is the process of converting a byte stream back into a python object, so that we can use it in our program. we can use pickle module to do this.

with open("p12_students.bin","br") as fs:
    '''
    data1 = pickle.load(fs)
    print(data1,type(data1))
    data2 = pickle.load(fs)
    print(data2,type(data2))
    data3 = pickle.load(fs)
    print(data3,type(data3))
    '''
    # data4 = pickle.load(fs)
    # print(data4,type(data4)) it will give EOFError : End of file reached, because we have only 3 objects in the file and we are trying to read 4 objects.

    # while True:
    #     try:
    #         data = pickle.load(fs)
    #         print(data,type(data))
    #     except EOFError:
    #         print("end of file reached...")
    #         break

# print the names of the students who secured 90 or more percentage...

    while True:
        try:
            data = pickle.load(fs)
            if data['percentage'] >= 90:
                print(data['name'])
        except EOFError:
            print("end of file reached...")
            break
        