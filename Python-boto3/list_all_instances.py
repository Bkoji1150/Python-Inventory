import boto3
import pprint

# aws_mag_con=boto3.session.Session()
# aws_con_re=aws_mag_con.resource(service_name='ec2',region_name="us-west-2")
# iam_con_client=aws_mag_con.client(service_name='ec2',region_name="us-west-2")
# aws_mag_client=aws_mag_con.client('sts')

# response =aws_mag_client.get_caller_identity()
# print("The account id is.....!")
# print(response.get('Account'))

import boto3

aws_con_re=boto3..resource(service_name='ec2',region_name="us-west-2")
ec2=aws_con_re.instances.all()

for i in ec2:
    print(i.id, i.state["Name"])
    # if i.state["Name"]=="stopped":
    #     i.start()
