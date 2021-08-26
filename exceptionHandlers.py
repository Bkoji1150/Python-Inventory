'''
Errors are two types:
      systax errors : --------->  no way to handle sysntax errors
      Runtime exceptions ----->   exceptions errors
'''
# print("Hello My name is Koji")
# print('Now it my time to Shine')
#
# try:
#     print(4/0)
# except:
#     print("Zero division erros")
'''
try:
    fo=open("naro.txt" 'r')
    print(fo,read())
    fo.close()
except:
    print("Please provide a valit file")
'''
try:
    print(a)
except Exception as e: # NameError, TypeError, Exception
    print(e)

#   Name error

try:
    print
