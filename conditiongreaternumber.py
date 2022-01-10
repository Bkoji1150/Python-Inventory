### Conditionals with python!
# a=eval(input("Enter your first number: "))
# b=eval(input("Enter your second number: "))
# if a > b:
#     print(f'{a} is greater than {b}')
# elif a < b:
#     print(f'{a} is less than {b}')
# else:
#     print(f'{a} and {b} are equals')
# READING NUMBERS
"""
num=eval(input("Enter Your number: "))
if num==1:
    print("one")
elif num==2:
    print("two")
elif num==3:
    print("Three")
elif num==4:
    print("four")
elif num==5:
    print("five")
elif num==6:
    print("six")
elif num==7:
    print("seven")
elif num==8:
    print("eight")
elif num==9:
    print("nine")
elif num==10:
    print("ten")
else:
    print(f"{num} is out of range, please select between 1-10")
"""

num=eval(input("Enter Your number: "))
if num in [1,2,3,4,5,6,7,8,9,10]:
    if num==1:
        print("one")
    elif num==2:
        print("two")
    elif num==3:
        print("Three")
    elif num==4:
        print("four")
    elif num==5:
        print("five")
    elif num==6:
        print("six")
    elif num==7:
        print("seven")
    elif num==8:
        print("eight")
    elif num==9:
        print("nine")
    else:
        print("ten")
else:
    print(f"{num} is out of range, please select between 1-10")

''' 
## Making use of Dictionary ....

num=eval(input("Enter Your number between 1-10 range: "))
my_dic={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}
if num in [1,2,3,4,5,6,7,8,9,10]:
    print(my_dic.get(num))
else:
    print(f"{num} is not in range of 1-10, please choose in range of 1-10")
    
'''