import boto3
import sys

session=boto3.session.Session()
ec2_con=session.resource(service_name='ec2',region_name='us-west-2')
ec2_con_client=session.client(service_name='ec2',region_name='us-west-2')

filer_test_enviroment={"Name":"tag:Env", "Values":['Prod']}
for i in ec2_con.instances.filter(Filters=[filer_test_enviroment]):
    instance_id=i.id
    print("Stopping ec2 instances..")
    i.stop()
    waiter=ec2_con_client.get_waiter('instance_stopped')
    waiter.wait(InstanceIds=[instance_id])
    print("Instance Stopped!")
    # if i.state.get('Name')=="running":
    #     print(f"{i.id}, The instance state is: {i.state.get('Name')}")
    #     print("Stopping instances in Test Env....")

else:
    print("Start ec2 instances....")
    i.start()
    waiter=ec2_con_client.get_waiter('instance_running')
    waiter.wait(InstanceIds=[instance_id])
    print("Instance running...")
    sys.exit()
