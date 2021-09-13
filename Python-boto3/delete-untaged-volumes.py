import boto3
aws_con_session=boto3.session.Session()
aws_con_re=aws_con_session.resource(service_name="ec2",region_name="us-west-2")
aws_con_cli=aws_con_session.client(service_name="ec2",region_name="us-west-2")
f_ebs_unused={"Name": "status", "Values": ["available"]}


for each_volumes in aws_con_re.volumes.all():
    if not each_volumes.tags:
        print(each_volumes.id,each_volumes.state,each_volumes.tags)
        print("Deleting unsed and untaged volumes...")
        each_volumes.delete()
print("Deleted all unused and untaged volumes!")

