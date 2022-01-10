import sys
import boto3
from pprint import pprint
aws_mag_con=boto3.session.Session()
aws_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-west-2")
aws_con_client=aws_mag_con.client(service_name="ec2",region_name="us-west-2")


f12={"Name": "instance-state-name", "Values": ['stopped']}
f2={"Name": "instance-type", "Values": ['t2.small']}
f3={"Name": "instance-type", "Values": ['t2.large']}


# Stopping in ec2 instance
no_prod_ids=[]
instance_ids_ = []
__all_instance_status = []
f1={"Name": "tag:env", "Values": ['sbx']}
list_of_tags = []
for each in aws_con_re.instances.filter(Filters=[f1]):

    for each_tags in each.tags:
        list_of_tags.append(each_tags['Value'])
print(list_of_tags)
#     no_prod_ids.append(each.id)
#     instance_ids_.append(each.state)
#
# for r in instance_ids_:
#     __all_instance_status.append(r.get('Name'))
#
#
# print(__all_instance_status)
# print(no_prod_ids)
# print(f"There are {len(no_prod_ids)} Instances")
# for each_healty in __all_instance_status:
#     if 6!= len(no_prod_ids) and each_healty!='running':
#         print(f"The are {len(no_prod_ids)} Instances Unhealty, Instances id are {no_prod_ids}")
#     else:
#         print(f"There are {len(no_prod_ids)} Healthy Instances")

print("Instances are stopping....")
aws_con_client.stop_instances(InstanceIds=no_prod_ids)
waiter=aws_con_client.get_waiter('instance_stopped')
waiter.wait(InstanceIds=no_prod_ids)
print("Your instances are stopped...")
#
# # changing instance type
#
# for i in no_prod_ids:
#     aws_con_client.modify_instance_attribute(InstanceId=i, Attribute='instanceType',Value='t2.large')
#
#
# #starting
# for each in aws_con_re.instances.filter(Filters=[f1]):
#     no_prod_ids.append(each.id)
# # print(no_prod_ids)
# print("Instances are starting....")
# aws_con_client.start_instances(InstanceIds=no_prod_ids)
# waiter=aws_con_client.get_waiter('instance_running')
# waiter.wait(InstanceIds=no_prod_ids)
# print("Your instances are started...")
# print("Your instance is now <<t2.large>>")
#
# # charging to t2.xlarge
# for instance_type in aws_con_re.instances.filter(Filters=[f3]):
#     for a in instance_type.id:
#         print("Instances are stopping....")
#         aws_con_client.stop_instances(InstanceIds=no_prod_ids)
#         waiter = aws_con_client.get_waiter('instance_stopped')
#         waiter.wait(InstanceIds=no_prod_ids)
#         print("Your instances are stopped...")
#         for change_and_resize in a:
#             aws_con_client.modify_instance_attribute(InstanceId=i, Attribute='instanceType', Value='t2.xlarge')
#             print("Instances are starting....")
#             aws_con_client.start_instances(InstanceIds=no_prod_ids)
#             waiter = aws_con_client.get_waiter('instance_running')
#             waiter.wait(InstanceIds=no_prod_ids)
#             print("Your instances are started...")
#             print("Your instance is now <<t2.xlarge>>")
#             sys.exit()





