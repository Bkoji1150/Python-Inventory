import boto3
import sys
from pprint import pprint

aws_mag_con= boto3.session.Session()
aws_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-west-2")
ec2_mag_cli=aws_mag_con.client(service_name='ec2',region_name='us-west-2')



aws_resource_object=aws_con_re.Instance('i-0039ecb2343c6f6b0')
Enter_your_choice=input("Please Enter <<Yes>> To start your instance and <<No>> to stop your instance: ")

if 'Yes'==Enter_your_choice:
    print("You have successfully start your instance------> ")
    print(aws_resource_object.state['Name'])
    sys.exit()
    # aws_resource_object.start()
    # print("Your instance is running")
if 'No'==Enter_your_choice:
    print('You have successfully stop your instance------> ')
    aws_resource_object.stop()
    print("Your instance is stopping")
else:
    print("Your provided invalit option")



while True:
    print('This script perform the following ations on ec2 Instance')
    print("""
        1. stop
        2. start
        3. resize_to_t2_large
        4. terminate
        """)
    opt=int(input("Enter your option: "))
    if opt==1:
        instance_id=input("Enter your instanceId: ")
        my_req_object= aws_con_re.Instance(instance_id)
        print(my_req_object.stop())
        print("starting ec2 instance........")
        sys.exit()
    elif opt==2:
        Instance_Id=input("Enter your instanceId: ")
        my_req_object = aws_con_re.Instance(Instance_Id)
        print(my_req_object.start())
        print("print starting ec2 instance-------")
    elif opt==3:
        Instance_Id=input("Enter your instanceId: ")
        print('resizing ec2 instance from t2.mricro to t2.large--------')
    elif opt==4:
        Instance_Id=input("Enter your instanceId: ")
        print('terminating ec2 instance------ ')
    else:
        print(f'{opt} is an invalit option')
        sys.exit()
