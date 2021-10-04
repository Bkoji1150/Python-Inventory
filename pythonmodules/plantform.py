import platform as pt
import getpass as gp

db_pass=gp.getpass(prompt="Enter your database password: ")

print(f"The db_password is...: {db_pass}")

# if pt.system()=="Windows":
#     print("Your are working with windows...!")
# else:
#     print("You you os isn't windows")
# print(f"The os you are working on is:{pt.machine()}\n And here is your release:{pt.release()}\n and the processor is: {pt.processor()}\n and the uname is: {pt.node()}"
#       f"The uname is: {pt.uname()}")