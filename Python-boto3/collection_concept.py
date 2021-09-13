import sys
import boto3
import pprint
aws_mag_con=boto3.session.Session()
aws_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-west-2")
aws_con_client=aws_mag_con.client(service_name="ec2",region_name="us-west-2")


f12={"Name": "instance-state-name", "Values": ['stopped']}
f2={"Name": "instance-type", "Values": ['t2.small']}
f3={"Name": "instance-type", "Values": ['t2.large']}


# Stopping in ec2 instance
no_prod_ids=[]
f1={"Name": "tag:Name", "Values": ['no-prod']}

for each in aws_con_re.instances.filter(Filters=[f1]):
    no_prod_ids.append(each.id)
# print(no_prod_ids)
print("Instances are stopping....")
aws_con_client.stop_instances(InstanceIds=no_prod_ids)
waiter=aws_con_client.get_waiter('instance_stopped')
waiter.wait(InstanceIds=no_prod_ids)
print("Your instances are stopped...")

# changing instance type

for i in no_prod_ids:
    aws_con_client.modify_instance_attribute(InstanceId=i, Attribute='instanceType',Value='t2.large')


# starting
for each in aws_con_re.instances.filter(Filters=[f1]):
    no_prod_ids.append(each.id)
# print(no_prod_ids)
print("Instances are starting....")
aws_con_client.start_instances(InstanceIds=no_prod_ids)
waiter=aws_con_client.get_waiter('instance_running')
waiter.wait(InstanceIds=no_prod_ids)
print("Your instances are started...")
print("Your instance is now <<t2.large>>")

# charging to t2.xlarge
for instance_type in aws_con_re.instances.filter(Filters=[f3]):
    for a in instance_type.id:
        print("Instances are stopping....")
        aws_con_client.stop_instances(InstanceIds=no_prod_ids)
        waiter = aws_con_client.get_waiter('instance_stopped')
        waiter.wait(InstanceIds=no_prod_ids)
        print("Your instances are stopped...")
        for change_and_resize in a:
            aws_con_client.modify_instance_attribute(InstanceId=i, Attribute='instanceType', Value='t2.xlarge')
            print("Instances are starting....")
            aws_con_client.start_instances(InstanceIds=no_prod_ids)
            waiter = aws_con_client.get_waiter('instance_running')
            waiter.wait(InstanceIds=no_prod_ids)
            print("Your instances are started...")
            print("Your instance is now <<t2.xlarge>>")
            sys.exit()





