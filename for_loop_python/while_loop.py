
import time,datetime,sys,os
# dt_convert=datetime.datetime.now().strftime("%y-%m-%d")
# dt_con=datetime.datetime.fromtimestamp(os.path.getctime())

# while False:
#     print("Welcome home!")
#     time.sleep(1)
req_path=input("Enter your path: ")
if not os.path.exists(req_path):
    print("Please provide valid path")
    sys.exit(1)
if os.path.isfile(req_path):
    print("Please provide directory path ")
    sys.exit(2)
today=datetime.datetime.now()
for each_file in os.listdir(req_path):
    each_file_path=os.path.join(req_path,each_file)
    if os.path.isfile(each_file_path):
        file_cre_date=datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
        dif_in_days=(today-file_cre_date).days
        if dif_in_days >= 1:
            print(each_file_path,dif_in_days)
            # sys.exit(3)
