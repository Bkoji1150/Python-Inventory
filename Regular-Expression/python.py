import re
## The difference operations in python are:
## Regular expressions (RegEX)
## The regex is a procedure in any language to look for a specified pattern in
##   a given text
'''
   match()
   search()
   findall()
   findall()
   finditer()
   sub()
   split()
   compile()...etc
  '''
text='This is python and it is easy to learn '
my_pat='i[ts]'
# print(len(re.findall(my_pat, text)))
print(re.findall(my_pat, text))
