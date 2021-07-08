import boto3
client = boto3.client('ec2', region_name='us-east-1')

def lambda_handler(event, context):
    response = client.start_instances(
        InstanceIds=['i-0e4409402ef0b9382'],
        AdditionalInfo='string',
        DryRun=False)
    