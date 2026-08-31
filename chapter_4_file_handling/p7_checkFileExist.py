# os.path.exists() is a function in the os.path module that checks if a specified file or directory exists. It returns True if the file or directory exists, and False otherwise.

# first method :
# import os

# os.path.exists()
# filePath1 = "C:/python course/chapter_4_file_handling/p7_checkFileExist.py"
# filePath2 = "p1.txt"
# if os.path.exists(filePath1 and filePath2):
#     print(f"the file '{filePath1} and {filePath2} is exists.")
# else:
#     print("the both file does not exist.")



# =====================================================================================================


# second method :
# import os or ||
from pathlib import Path

filePath3 = Path("C:/python course/chapter_4_file_handling/p3.txt")

if filePath3.exists():
    print("The file is exists. Cannot create a new file with the same name.")
else:
    print("The file does not exists. Creating a new file.\n")
    fs = open(filePath3,'xt')
    fs.write("This is a new file created using the pathlib module.\n")
    fs.close()






