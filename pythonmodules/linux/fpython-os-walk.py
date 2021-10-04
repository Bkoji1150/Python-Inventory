import os
from moduleForPath import path1
# if os.path.isfile(path1)==True:
#     print(f'{path1}... this path is a file')
# else:
#
#     print(f'{path1}... this path is a directory')
for r,d,f in os.walk(path1,topdown=True):
    if len(f) !=0:
        print(f)
        for each_file in f:
            print(os.path.join(r,each_file))
