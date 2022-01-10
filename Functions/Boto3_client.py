import boto3
from pprint import pprint
aws_con = boto3.session.Session()


def list_buck_cli():
    li = []
    try:
        # Working with iam using boto3 client
       iam_cli = aws_con.client('iam')
       for users in iam_cli.list_users()['Users']:
           li.append(users['UserName'])
    except Exception as e:
            print(e)
    return li


def __cli_s3__():
    # Working with s3 using boto3 client
    try:
        s3_client = aws_con.client('s3')
        for buckets in s3_client.list_buckets()['Buckets']:
            print(buckets["Name"])
    except Exception as p:
        print(p)
    return None


def ec2_boto():
    # Working with ec2 instances using boto3 client
    try:
        ec2 = aws_con.client(service_name='ec2', region_name='us-west-2')
        response  = ec2.describe_instances()
        for each_items in response['Reservations']:
            for each_instances in each_items.get('Instances'):
                # pprint(each_instances)
                print(f"The instances images is: {each_instances.get('ImageId')}\nThe instance ids ares: {each_instances.get('InstanceId')}\nT"f"he launchTime is: {each_instances.get('LaunchTime').strftime('%y-%m-%d')}")
                print(f"The instance state shows: {each_instances.get('State')['Name']}")
                if each_instances.get('State')['Name']=='running':
                    print('The instance is show',each_instances.get('State')['Name'])
                    pass
                else:
                    print(f"The instance is in {each_instances.get('State')['Name']} state")
    except Exception as e:
        print(e)
    return None


def main():
    # calling s3 function and list_user function
    # __cli_s3__()
    ec2_boto()
    # print('list of users:',list_buck_cli())
    return None


if __name__=='__main__':
        main()
