import boto3
aws_mag_con = boto3.session.Session()


def main():
    # iam list users function
    iam_con = aws_mag_con.resource('iam')
    try:
        for each_user in iam_con.users.all():
            print(each_user.name)
        s3_buckets()
    except Exception as e:
        print(e)
    return None


def s3_buckets():
    s3 = aws_mag_con.resource('s3')
    # List s3 buckets function
    try:
        for each_buckets in s3.buckets.all():
            print(f"These are the list of s3:",each_buckets.name)
    except Exception as e:
        print(e)


try:
    if __name__=='__main__':
        main()
except Exception as e:
    print(e)
