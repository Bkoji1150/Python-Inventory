import json

'''
req_file=input("Please enter the path of your json file: ")

fo=open(req_file, 'r')
print(fo.read())

fo.close()
'''

req_file=input("Please enter the path of your json file: ")
target_path=input("Please Enter Your Target path: ")

fo=open(req_file, 'r')
dt=open(target_path, 'w')
pz=(json.load(fo).get('Parameters'))
json.dump(pz, dt,indent=4)

fo.close()
