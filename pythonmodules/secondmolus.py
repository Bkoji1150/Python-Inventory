# Python second modules
import firstmodule
not
print(firstmodule.num)
import os

path= input("Enter your path: ")

if os.path.exists(path):
    print(f'The given Path {path} is a valid path')
    if os.path.isfile(path):
        print("and is a file path")
    else:
        print("and is a directory")
else:
    print(f"Given path : {path} is not existing on the host")

import os,sys

path=input("Enter your directory path: ")
if os.path.exists(path):
    print(f"{path} is a valid path!")
    dt_t=(os.listdir(path))
dt_t1=os.path.join(dt_t[0])
if os.path.isfile(dt_t1):
    print(f'{dt_t1} is a file')
else:
    print(f'{dt_t1} is a directory')
import sys
print(sys.argv)
print(sys.argv[0])

import os
path="C:\\Users\\new\\Documents\\src\\pythonscripts\\pythonmodules"
# p1={"Africa":"Cameroon", "Nigeria", "Ghanna", "Garbon","Serialoen", "Asia":"india", "Chinna", "Japan")"}
# print(p1)
print(list(os.walk(path)))
print("--------------------------------")
for r,d,f in os.walk(path):
    if len(f) !=0:
        print(r)
        for i in f:
            print(os.path.join(r,i))
