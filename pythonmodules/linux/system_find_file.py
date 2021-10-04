import os
import string
import platform
import sys

if platform.system()=='Windows':
    pd_names=string.ascii_uppercase
    vd_names=[]
    for each_drive in pd_names:
        if os.path.exists(each_drive+":\\"):
            vd_names.append(each_drive+":\\")
            req_file=input("please Enter your file name to search: ")
            for each in vd_names:
                for r,d,f in os.walk(each):
                    for each_file in f:
                        if each_file==req_file:
                            print(os.path.join(r,each_file))
else:
    sys.exit(1)

# path=input("please Enter your file name to search: ")
# for r,d,f in os.walk("C:\\Users\\new\\"):
#     for each_file in f:
#         if each_file==path:
#             print(os.path.join(r,each_file))