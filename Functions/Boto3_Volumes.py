import boto3
from pprint import pprint
aws_con = boto3.session.Session()


def __volumes__():
    try:
        volumes = aws_con.client('ec2',region_name='us-west-2')
        response = volumes.describe_volumes().get('Volumes')
        for each_itemes in response:
            print(f"{each_itemes.get('Attachments')}\nThe Volume id is: {each_itemes['VolumeId']}")
            for i in each_itemes.get('Attachments'):
                print(i['VolumeId'])
                print(f"The volume state shows: {i['State']}")

    except Exception as e:
        print(e)


def main():
    __volumes__()
    return None


try:
    if __name__=='__main__':
        main()
except Exception as e:
    print(e)