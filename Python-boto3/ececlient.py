import boto3
from pprint import pprint

aws_mag_se_user= boto3.session.Session()
aws_con_rel=aws_mag_se_user.resource(service_name="ec2",region_name="us-west-2")
ec2_mag_con=aws_mag_se_user.client(service_name="ec2",region_name="us-east-1")

print(dir(aws_con_rel))
'''
response = ec2_mag_con.describe_instances()['Reservations']
for each in response:
    for each_int in each.get('Instances'):
        print(f"The Image id is: {each_int.get('ImageId')}\nThe Instance type is:{each_int.get('InstanceType')}\nThe Lauch date is: {each_int.get('LaunchTime').strftime('%Y-%m-%d')}\nThe Instance state is: {each_int.get('State')['Name']}")
'''
'''
response=ec2_mag_con.describe_volumes().get('Volumes')
for each_items in response:
    print(each_items.get('Size'))
'''
