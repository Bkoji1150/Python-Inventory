# Create a new file
# Add a content in an existing file
'''
fo=open('../love.py','w')
fo.write("This is first line\n")
fo.write("This is the second line\n")
fo.write("This is the third line")
fo.close()
'''
'''
my_content=["This is first line",'This is the second line','This is the third line']
fo=open('../love.py','a')
for each in my_content:
    fo.write(each+'\n')
fo.close()
'''
# import sys
# tb=open('../love.py','r')
# data=tb.readlines()
# tb.close()
#
# for each in range(3):
#     print(data[each])

source_file=input("Please enter your source file: ")
dfile='newdemo.txt'

sfo=open(source_file,'r')
content=sfo.read()
sfo.close()

dfo=open(dfile,'w')
dfo.write(content)
dfo.close()


# print(content.txt,'w')
# dfo.write(content)
