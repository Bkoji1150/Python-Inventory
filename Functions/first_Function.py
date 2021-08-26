'''
import os
import time
import platform
def mycode(cmd1,cmd2):
	print("Please wait. Cleaning the screen....")
	time.sleep(2)
	os.system(cmd1)
	print("Please wait finding the list of dir and files")
	time.sleep(2)
	os.system(cmd2)
if platform.system()=="Windows":
	mycode("cls","dir")
else:
	mycode('clear','ls -lrt')
'''
# def display():
#     print("You are the love of my life")
#     print("You are the woman of my dream")
#     return None
#
# display()

x=[5,6,100,223,345465,5,0]
print(len(x))
print(max(x))
print(min(x))
print(type(x))
