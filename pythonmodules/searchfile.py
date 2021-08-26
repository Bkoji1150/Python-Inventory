# import os
# req_file=input("Enter your file name to search: ")
# for r,d,f in os.walk("/home/ansible"):
#     for each_file in f:
#         print(os.path.join(r,req_file))

import os
import string
import platform
import sys
req_file=input("Enter your file name to search: ")

if platform.system()=="Windows":
    pd_names=string.ascii_uppercase
    vd_names=[]
    for each_file in pd_names:
        if os.path.exists(each_file+":\\"):
            vd_names.append(each_file+":\\")
    print(vd_names)
    for each_file in vd_names:
        for r,d,f in os.walk(each_file):
            for each_f in f:
                if each_f==req_file:
                    print(os.path.join(r,each_f))
                    print(sys.exit())
else:
    for r,d,f in os.walk("/"):
        for each_file in f:
            if each_file==req_file:
                print(os.path.join(r,each_file))
                if each_file!=req_file:
                    print("Sorry file doesn't exit")
