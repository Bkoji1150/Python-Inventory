

import os,sys
path=input("Enter your directory name to search: ")
if os.path.exists(path):
    df_1=os.listdir(path)
else:
    print("Please provide a valid path")
    sys.exit()

list_of_all_dir=os.listdir(path)
for each_file_or_dir in list_of_all_dir:
    f_d_p=os.path.join(path,each_file_or_dir)
    if os.path.isfile(f_d_p):
        print(f'{f_d_p} is a file')
    else:
        print(f'{f_d_p} is a directory')
