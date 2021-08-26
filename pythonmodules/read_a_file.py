import os

path=input("Enter your file name to search: ")
if os.path.exists(path):
    print(f"Given path: {path} is valit")
    print("++++++++++++++++++++++++++++++++++++++")
    if os.path.isfile(path):
        print(f'The given file path: {path} is a file')
    else:
        print(f'The given file path: {path} is a directory')
else:
    print(f"Your path: {path}   doesn't  exit")

'''
if os.path.isfile(path):
    print(f'The given file path: {path} is a file')
else:
    print(f'The given file path: {path} is a directory')
'''
