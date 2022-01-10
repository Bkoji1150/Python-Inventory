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
try:
    source_file = ''
    _f = 'reading_file.py'
    my_content = ["This is first line", 'This is the second line', 'This is the third line']
    dfile='file1'

    # sfo=open(source_file,'r')
    df = open(dfile, 'w')
    ''' 
    df.write('This is the first name\n')
    df.write("I'm coming home")
    print(dir(df))
    '''
    for i in my_content:
        df.writelines(i+"\n")
    # content=sfo.read()
    # print(sfo.readable())
    df.close()
    # sfo.close()
    my_content = ["This is first line", 'This is the second line', 'This is the third line']
    fo = open(_f, 'a')
    for each in my_content:
        fo.write(each + '\n')
    fo.close()
except Exception as e:
    print(e)

# dfo=open(dfile,'w')
# dfo.write(content)
# dfo.close()


# print(content.txt,'w')
# dfo.write(content)
