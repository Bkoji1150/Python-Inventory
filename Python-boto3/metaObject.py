import boto3
import pprint
aws_mag_con=boto3.session.Session()
aws_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-west-2")

for each in aws_con_re.meta.client.describe_regions()['Regions']:
    print(each.get("RegionName"))
