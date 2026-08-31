# print all file names that is in the directory using importing os model

import os

# specify the directory you want to list
directory_path = '/python course'

# list all files and directory in the specified path
contents = os.listdir(directory_path)

# print each file and director name
for item in contents:
    print(item)
    
    
'''
'''