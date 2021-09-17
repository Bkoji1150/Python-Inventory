try:
    import boto3, sys, botocore

except ModuleNotFoundError:
    print("boto3 not found please review and try again")
except Exception as e:
    print(e)
    sys.exit(1)
try:
    aws_mag_con=boto3.session.Session()
except botocore.exceptions.ProfileNotFound:
    print("The provided user isn't configured please provided a valid users")
    sys.exit(2)
except Exception as e:
    print(e)
    sys.exit(4)
try:
    iam_con_user=aws_mag_con.resource(service_name="iam")
    for i in iam_con_user.users.all():
        print(i)
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code']=="AccessDenied":
        print("The required user have got no permissions on required service")
    else:
        print(e.response['Error']['Code'])
    sys.exit(5)
