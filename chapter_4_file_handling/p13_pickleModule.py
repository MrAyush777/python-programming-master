import pickle

students = {
            'student1' : {'rollNo' : 1, 'name' : 'Ayush', 'percentage' : 90},
            'student2' : {'rollNo' : 2, 'name' : 'Mahi', 'percentage' : 80},
            'student3' : {'rollNo' : 3, 'name' : 'Ram', 'percentage' : 100}
        }

# print(students, type(students))

# with open('p13_students.txt','wt') as fs:
#     fs.write(str(students))

# with open('p13_students.txt','rt') as fs:
#     data = fs.read()

# print(data, type(data))
# output = dict(data) # it will not work as data is a string and we cannot convert it to dict directly. it will give an error.
# print(output)


# ================================= WE WILL USE PICKLE MODULE TO SOLVE THIS PROBLEM =================================


# with open('p13_pickleModule.bin','bx') as fs:
with open('p13_pickleModule.bin','bw') as fs:
    for student in students:
        pickle.dump(students[student],fs)

with open('p13_pickleModule.bin','rb') as fs:
    # data1 = pickle.load(fs)   
    # data2 = pickle.load(fs)   
    # data3 = pickle.load(fs)   
    # print(data1)
    # print(data2)
    # print(data3)

    for data in fs:
        print(pickle.load(data))