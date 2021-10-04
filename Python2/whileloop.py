# i = 1
#
# while i <= 5:
#     print("*" * i)
#     i += 1
# print('Done!')

secret_num= 9
user_coun=0
user_limit=3

while user_coun < user_limit:
    guess_cout = int(input('Please enter the secret number: '))
    user_coun += 1
    if guess_cout == secret_num:
        print("You won")
        break
else:
    print("please try again!!")
