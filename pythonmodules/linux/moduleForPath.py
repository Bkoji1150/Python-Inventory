try:
    import os
except Exception as e:
    print(e)
# path="C:\\Users\\new\\Documents\\src\\Python-Inventory\\venv\\Scripts"

path1="C:\\Users\\new\\Documents\\src\\TERRAFORM-GIT-MODULE\\Terraform-Ecs-Fargate\\ecs\\"
# print(os.path.dirname(path)) This is to get the directory name
# print(os.path.basename(path))
# print(os.path.join(path1, path2))
# print(os.path.join(path1,path2)) # These paths are strings...
# print(os.path.split(path2)) it would give a tupple
# get size print(os.path.getsize("C:\\Users\\new\Documents\\src\\Python-Inventory"))
'''
# This is to check is the path exist
if os.path.exists("C:\\Users\\new\Documents\\src\\Python-Inventorywe")==True:
    print("Your file is there")
else:
    print
path="C:\\Users\\new\Documents\\src\\Python-Inventory"
'''

'''
This is to check this the path is a file of directory
'''
path=input("Please enter file to search: ")
''' 
if os.path.isfile(path)==True:
    print(f'{path}: This current path is a file')
else:
    print(f'{path}: this current directory is a directory')
'''
# if os.system('date')==0:
#     print("your command was successfully executed")
#     os.system('date')
# else:
#     print("The command your run is unsuccessful")
