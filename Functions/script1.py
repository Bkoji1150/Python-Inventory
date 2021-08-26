###
def addition(a,b):
    print(f"The addition of {a} and {b} is : {a+b}")
    return None
def subtraction(a,b):
    print(f'The subtraction of {a} and {b} is: {a-b}')
    return None
# def mult(a,b):
#     print(f'The multiplication of {a} and {b} is: {a*b}')
#     return None

def main():
    a=eval(input("Enter first value: "))
    b=eval(input('Enter second value: '))
    addition(a,b)
    subtraction(a,b)
    # mult(a,b)
    return None
if __name__=='__main__':
    main()

if __name__=="__main__":
    print('This is from script1',__name__)
