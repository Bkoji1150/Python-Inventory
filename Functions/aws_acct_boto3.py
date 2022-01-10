import boto3
aws_mag_con = boto3.session.Session()


def __aws_acc_id__():
    try:
        client = aws_mag_con.client(service_name='sts',region_name='us-west-2')
        response = client.get_caller_identity()
        for i,e in response.items():
            print(f"{i}, {e}")
        print("this is your acct id:",response.get('Account'))
        print(response.get('ResponseMetadata')['RequestId'])
    except Exception as p:
        print(p)
    return None


def main():
    __aws_acc_id__()


try:
    if __name__=='__main__':
        main()
except Exception as e:
    print(e)
