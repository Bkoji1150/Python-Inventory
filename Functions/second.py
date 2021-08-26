import script1

# print(dir(script1))
def mult(a,b):
    print(f'The multiplication of {a} and {b} is: {a*b}')
    return None

a=eval(input("Enter first value: "))
b=eval(input('Enter second value: '))

def main():
    script1.addition(a,b)
    # script1.subtraction(a,b)
    # mult(a,b)
    return None
if __name__=='__main__':
    main()

if __name__=="__main__":
    print('this is from script2',__name__)
