## User actions on script
"""
usr_input=input("Please enter you string values: ")
convert_in_string=input("Please choose if you would like to convert into a lower/upper/title: ")
if convert_in_string=="lower":
    print(f'your string\t "{usr_input.lower()}" have been converted into lower case')
elif convert_in_string=="upper":
    print(f'your string\t "{usr_input.upper()}" have been converted into upper case')
elif convert_in_string=="title":
    print(f'your sting\t "{usr_input.title()}" have been converted into tittle format')
else:
    print("Please choose withing the valit values which are lower,upper, title")
"""

#usr_input=input("Please enter you string values: ")
#convert_in_string=input("Please choose if you would like to convert into a lower/upper/title: ")

import sys
if len(sys.argv) !=3:
    print("Usage: ")
    print(f'{sys.argv[0]} <Please select amoung> <lower|upper|title>')
    sys.exit()

usr_input=sys.argv[1]
convert_in_string= sys.argv[2]

if convert_in_string=="lower":
    print(f'your string  "{usr_input.lower()}" have been converted into lower case')
elif convert_in_string=="upper":
    print(f'your string  "{usr_input.upper()}" have been converted into upper case')
elif convert_in_string=="title":
    print(f'your sting  "{usr_input.title()}" have been converted into tittle format')
else:
    print(f"<{usr_input}> is incorrect, Please choose within the valit values: which are <lower/upper/title>")
