import os, time, platform

def mycode(cmd1,cmd2):
    print('Please wait. Cleaning screen....')
    time.wait(2)
    os.system(cmd1)
    print('Please wait. Cleaning screen....')
    time.wait(3)
    os.system(cmd2)

if platform.system()=="Windows":
    mycode('dir','cls')
else:
    mycode('ls -lrt','clear')
