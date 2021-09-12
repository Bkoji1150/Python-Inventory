import boto3, pprint
aws_mag_con=boto3.session.Session()
aws_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-west-2")

f1={"Name": "instance-state-name", "Values": ['stopped']}
f2={"Name": "instance-type", "Values": ['t2.small']}
for each in aws_con_re.instances.filter(Filters=[f2]):
    print(each)
