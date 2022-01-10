import boto3
aws_mag_con = boto3.session.Session()


def __list_iam_users__():
    # Working with iam using boto3 resource object
    try:
        iam = aws_mag_con.resource('iam',region_name='us-west-2')
        respones = iam.users.all()
        for list_of in respones:
            print(list_of.user_name)
    except Exception as e:
        print(e)


def __list_s3_buckets__():
    try:
        s3 = aws_mag_con.resource('s3', region_name='us-west-2')
        list_bu = []
        for each_buckets in s3.buckets.all():
            list_bu.append(each_buckets.name)
    except Exception as e:
        print(f"Error while running: {e}")
    return list_bu


def __list_ecs_re():
    try:
        ec2 = aws_mag_con.resource('ec2', region_name='us-west-2')
        for all_instances in ec2.instances.all():
            print(all_instances.instance_id)
    except Exception as p:
        print(p)


def main():
    # __list_iam_users__()
    list_ = __list_s3_buckets__()
    __list_ecs_re()
    return None


try:
    if __name__=='__main__':
        main()
except Exception as e:
    print(e)







