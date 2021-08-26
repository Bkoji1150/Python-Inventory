import re
def get_add(value):
    result=value+10
    print(f'Your result is: {result}' )
    return None
def my_code():
    # global num
    num=eval(input("Enter an input: "))
    get_add(num)
    return None
my_code()
