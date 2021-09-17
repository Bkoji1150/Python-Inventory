from random import choice
len_of_password=18
valid_passwd="qedanwkaqsrfdxzcvghtrewqw@!~`!2_+_,<''>y98785y34566\AX;RVZMdcla"

password=[]
for each_char in range(len_of_password):
    password.append(choice(valid_passwd))
random_passwd=("".join(password))
print(random_passwd)
print("------")
