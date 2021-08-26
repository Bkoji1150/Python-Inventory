### how to run system command with python!
import os
cmd=input("Please enter a  valit command: ")
rt=os.system(cmd)
if rt==0:
    print("Your commad was executed succesfully: ")
else:
    print("invalid Cammand! ")
