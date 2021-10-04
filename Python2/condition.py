'''
If name is less than 3 characters long
  name must be at least 3 charaters
otherwise if it's more than 50 characters long
  name can be a maximum of 50 characters
otherwise
   name looks good!
'''
'''
user_name=input('Enter user name: ')

if len(user_name)<3:
    print("name must be at least 3 charaters")
elif len(user_name)>10:
    print("name can be a maximum of 10 characters")
else:
    print("name looks good!")

'''
#ask user to enter weight and convert
'''
'''
weight = eval(input('Enter your weight: '))
unit = input('(L)bs or (K)g: ')

if unit.upper()=="L":
    converted = weight * 0.45
    print(f"your weight is : {converted}")


