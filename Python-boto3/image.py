import boto3, botocore
session=boto3.session.Session()
client= session.client(service_name="ec2", region_name="us-west-2")

instance_list=[]
instance_id=[]

for instances in client.describe_instances()['Reservations']:
    for i in instances.get('Instances'):
        instance_list.append(i.get('ImageId'))
        instance_id.append(i.get('InstanceId'))
print(f"The image ids are: {instance_list}\nThe instance types are: {instance_id}")




# try:
#     response = client.create_image(
#         InstanceId=instance_id[0],
#         Name='test'
#     )
# except Exception as e:
#     print(e)