import csv
# req_file=input("Enter your csv file: ") #C:\Users\new\Downloads\Bello_accessKeys.csv
#
# fo=open(req_file, 'r')
# data=csv.reader(fo,delimiter=",")
#
# for each in data:
#     print(each)
# fo.close()

# req_file="C:\\Users\\new\\Documents\\src\\new_info.csv"
#
# fo=open(req_file, 'w')
# csv_writer=csv.writer(fo,delimiter=",")
# csv_writer.writerow(['First_Name','Last_Name','Date_Of_Birth'])
#
# fo.close()

req_file=input('Please enter path, to create a file: ')
cs=open(req_file, 'w',newline="")
csv_writer=csv.writer(cs,delimiter=",")
csv_writer.writerow(['First_Name','Last_Name','Employee','Salary','Insurance'])
csv_writer.writerow(['Koji','Bello','DBA','140,0000','Kaiser'])

cs.close()
