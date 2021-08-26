'''
 def get_addition(d,t):
    result=d+t
    # print(f'The addition of {a} + {b} is equal: {result}')
    return result

def main():
    a=eval(input("Enter your first number: "))
    b=eval(input("Enter your second number: "))
    result=get_addition(a,b)
    print(f'The addition of {a} + {b} is equal: {result}')
    return None
main()
'''

def multi_value(num):
    return num*10

def main():
    num=eval(input('Enter your number: '))
    result=multi_value(num)
    print("The result is:", result)

main()
