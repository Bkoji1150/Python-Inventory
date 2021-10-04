import boto3
session=boto3.session.Session()
iam_con_re=session.resource(service_name="iam")

#Get details of any iam users

# iam_user_ob=iam_con_re.User("Koji-dba")
# print(dir(iam_user_ob))

for each_user in iam_con_re.Users.all():
    print ("UserName={} UserId={} User ARN={} User Creation Date={}".format(each_user.user_name,each_user.user_id,each_user.arn,each_user.create_date))
    # print(each_user.user_id)
