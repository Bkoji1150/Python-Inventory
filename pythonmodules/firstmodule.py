### Python modules
num=eval(input("Enter Your number between 1-10 range: "))
my_dic={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}
if num in [1,2,3,4,5,6,7,8,9,10]:
    print(my_dic.get(num))
else:
    print(f"{num} is not in range of 1-10, please choose in range of 1-10")
