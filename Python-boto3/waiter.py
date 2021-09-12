"""
session
Resource
client
Meta
Collections
Waiters
Paginations
"""

import boto3
import time
aws_mag_se_user= boto3.session.Session()
aws_con_rel=aws_mag_se_user.resource(service_name="ec2",region_name="us-west-2")
ec2_mag_cli=aws_mag_se_user.client(service_name="ec2",region_name="us-west-2")

print("Stopping instance....")
my_req_object=aws_con_rel.Instance("i-08e2d85419cb5a8c4")
my_req_object.stop()
waiter=ec2_mag_cli.get_waiter('instance_stopped')
waiter.wait(InstanceIds=['i-08e2d85419cb5a8c4'])
print("Instance Stopped")


'''
object_of_console=aws_con_rel.Instance('i-08e2d85419cb5a8c4')
print("Starting given instance..............")
object_of_console.start()
object_of_console.wait_until_running()
print("Your instance is in running state!")
'''



''' 
while True:
    object_of_console = aws_con_rel.Instance('i-0039ecb2343c6f6b0')
    print("The current status is: ",object_of_console.state['Name'])
    if object_of_console.state['Name']=="running":
        break
        print('waiting for instance to show running')
        time.sleep(5)
print("Now your ec2 instance is running")

for each in object_of_console:
    print(each)
'''
