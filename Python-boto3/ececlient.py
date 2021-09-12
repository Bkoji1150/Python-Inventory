import boto3
from pprint import pprint

aws_mag_con_user= boto3.session.Session()
ec2_mag_con=aws_mag_con_user.client(service_name='ec2', region_name='us-west-2')

response = ec2_mag_con.describe_instances()['Reservations']
for each in response:
    for each_int in each.get('Instances'):
        print(f"The Image id is: {each_int.get('ImageId')}\nThe Instance type is:{each_int.get('InstanceType')}\nThe Lauch date is: {each_int.get('LaunchTime').strftime('%Y-%m-%d')}\nThe Instance state is: {each_int.get('State')['Name']}")
