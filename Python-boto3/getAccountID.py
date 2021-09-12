import boto3

aws_mag_con_user= boto3.session.Session(profile_name="koji-devops")
aws_mag_con= boto3.session.Session()
aws_mag_client=aws_mag_con.client('sts')

response =aws_mag_client.get_caller_identity()
print(response.get('Account'))
print(response.get('Arn'))
