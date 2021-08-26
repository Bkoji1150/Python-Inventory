# #####
#
# import os
# import string
# import platform
#
# for r,d,f in os.walk("/"):
#     for each_file in f:
#         print(r,os.walk)


# python.py
# secondmolus.py
# searchfile.py
# Welcome
# action_on_string.py
# basic-operator.py
# A hackable text editor for the 21st Century
# For help, please visit
#
# The Atom docs for Guides and the API reference.
# The Atom forum at discuss.atom.io
# The Atom org. This is where all GitHub-created Atom packages can be found.
# Show Welcome Guide when opening Atom
# atom.io ×
# run_any_cmd.py
# pythonmodule.py
# Welcome Guide
# dictionary.py
# function.py
# firstmodule.py
# searchfile.py
# platform-independent.py
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
#####

import os
import string
import platform

for r,d,f in os.walk("/"):
    for each_file in f:
        print(r,os.walk)



import os
import string
import platform
if platform.system()=='Linux':
    user_import=input('Enter a file name: ')
    for r,d,f in os.walk("/"):
        for each_file in f:
            if each_file==user_import:
                print(os.path.join(r,each_file))

if each_file!=user_input:
    print("File doesn't exist!")
