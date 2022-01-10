import boto3, pprint
session=boto3.session.Session()
con_re=session.resource(service_name='ec2', region_name='us-west-2')


def list_of_buckets():
    list_of_buckets = []
    s3 = session.client(service_name='s3', region_name='us-west-2')
    try:
        for i in s3.list_buckets()["Buckets"]:
            list_of_buckets.append(i.get("Name"))
    except Exception as e:
        print(e)
    return list_of_buckets


b = list_of_buckets()
print(f"{b},\n Your have {len(b)} buckets in your acct")



def main():
    pass


if __name__=='__main__':
    main()




