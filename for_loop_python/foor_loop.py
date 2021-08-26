### Loop in python

# my_list={"Africa":["Cameroon","Nigeria","Ghanna","Mali"],"Asia":["India","Japan","China"]}
# print(type(my_list))
# print(my_list.values)

# my_list=input("Enter loop: ")
# # print(len(my_list))
#
# print("+++++++++++++++++++++++++++++++++++++")
# for each_values in my_list:
#     print("python",my_list)

# my_list=input("Enter value: ")
# rem=my_list%2
# if rem==0:
#     print(f'{my_list} is an even')
# else:
#     print(f'{my_list} is an odd')

# index=0
# for i in my_list:
#     print(f"{my_list} ----->{index}")
#     index=index+1

magic_number='brontech1'
guess= ""
index=3
while guess !=magic_number and index!=0:
    guess = input("Enter your password: ")
    index -=1
    if index<0:
        print('Sorry you have exhausted the limit of 3')
        break
    if guess==magic_number:
        print("login succesful!")
    else:
        print(f"Incorrect password, please try again:\n You Have {index} Atempt left")
