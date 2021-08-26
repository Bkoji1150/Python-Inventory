## count and index
"""
x = 'Python is the most popular lan'
# print(x.count('p'))

print(x.find('the'))
"""
"""
    ### Displace Given line in left, Right, center and title
"""
#
# import os
# t_w=os.get_terminal_size().columns
# x = input('Enter you desired words: ') #"Python is my best programming language!"
# usr_confrm= input('Please confirm:\n yes or no: ?')
# if usr_confrm=="yes":
#     print(x.center(t_w).title())
#     print(x.rjust(t_w).title())
#     print(x.ljust(t_w).title())
# else:
#     print("You fail!")
# b=eval(input('Enter you desired valued:\n '))
# a=eval(input('Second value:\n '))
# operators= [*,+,/,-]
# print(operators)
# usr_str=input("Enter you string: ")
# usr_conf=input("Do you want to convert your string into lower case?, say yes(y) or no(y)!")
# if usr_conf=="yes":
#     print(usr_str.lower())
# else:
#     print('As you desired!')

# even_num=[0,2,4,6,8,10,12,14]
# usr_even=eval(input("Enter user input\t "))
# if usr_even in even_num:
#     print("You've printed an even number!")
# else:
#     print("Sorry you didn't print an even number!")""
"""
list_of_african_countries=["cameroon", "ghana", "nigeria","serialoean", 'zimbabew', "zenya","ivory coast"]
usr_list_of_african_countries=str(input("Please put an african country:\t "))
if usr_list_of_african_countries in list_of_african_countries:
    print(f"You have choosen an African Country! {usr_list_of_african_countries} ")
else:
    print(f"Sorry!, {usr_list_of_african_countries} is not in {list_of_african_countries}")
"""
usr_str=str(input("Enter you string:\t"))
usr_confrm=input("Do you want to convert to string? say yes or no: ")
if usr_confrm=="yes":
    print(usr_str.title())
else:
    print(usr_str)
