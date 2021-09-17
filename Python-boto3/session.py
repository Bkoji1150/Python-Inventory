#
# aws configure --profile "koji-devops"
====================================================
# Custom Session:
#
# import boto3
# aws_mag_con=boto3.session.Session(profile_name="koji-devops") # customer session
# aws_mag_con=boto3.session.Session() # default session
#
# # print(aws_mag_con)
#
# iam_con_re=aws_mag_con.resource(service_name='iam',region_name="us-east-1")
# print(iam_con_re)
# iam_con_client=aws_mag_con.client(service_name='iam',region_name="us-east-1")
# #
# for each_user in iam_con_re.roles.all():
#     print(each_user.name)


# print(iam_con_re)

# ===============================================================================
# Default:
#
# import boto3
# iam_con_re=boto3.resource(service_name="iam",region_name="us-east-1")
#
# ===============================================================================
#
#
# import boto3
# aws_mag_con=boto3.session.Session(profile_name="root")
#
# ec2 = aws_mag_con.resource('ec2')

import boto3

aws_mag_con= boto3.session.Session()
iam_con_client=aws_mag_con.client('iam', region_name='us-west-2')
ec2_con_client=aws_mag_con.client('ec2', region_name='us-west-2')
s3_con_client=aws_mag_con.client('s3', region_name='us-west-2')


# list all iam users using client object
'''
response=iam_con_client.list_users()
for each_iteams in response['Users']:
    print(each_iteams['UserName'])
'''

### List all ec2 display_details

'''
response=ec2_con_client.describe_instances()

for each in response['Reservations']:
    for each_intsance in each['Instances']:
        print(each_intsance['InstanceId'])
    print('==================================')
'''

### List s3 bucket

# list_of_buckets=[]
#
# response=s3_con_client.list_buckets()
# # response_of_objects=s3_con_client.list_objects(Bucket=list_of_buckets)
# for each_bucket in response['Buckets']:
#     count=0
#     # creation_date=each_bucket['CreationDate']
#     bucket_names=each_bucket['Name']
#     print(bucket_names)


    # list_of_buckets= bucket_names
    # for i in response_of_objects['Contents']:
    #     print(f"The contects of bucket {list_of_buckets} are ---->", i['Key'])
    #



bucket3='hap23bdv-bucket'


# for each in bucket3:
#     print(each)
response=s3_con_client.list_objects(Bucket=bucket3)

for i in response['Contents']:
    print(f"The contects of bucket {bucket3} are ---->",i['Key'])
