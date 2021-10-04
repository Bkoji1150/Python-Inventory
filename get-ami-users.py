import boto3, pprint
session=boto3.session.Session()
s3_con_re=session.resource(service_name='ec2', region_name='us-west-2')
s3_con_client=session.client(service_name='s3', region_name='us-west-2')
# we are using resource object to list our buckets
''''
for each_bucket in s3_con_re.buckets.all():
    print(each_bucket.name)
'''
# Now let us use client resource to archive thesame result
''' 
for each_buckets in s3_con_client.list_buckets()['Buckets']:
    print(each_buckets['Name'],each_buckets['CreationDate'])
'''
for each_image in s3_con_re.images.filter():
    print(each_image)