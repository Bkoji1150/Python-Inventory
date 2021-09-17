

# [root]
# aws_access_key_id = AKIAJRCMPX5GEZQLWWTA
# aws_secret_access_key = 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
# [ec2_developer]
# aws_access_key_id = AKIA5XNJJZL57MQ4WGWM
# aws_secret_access_key = 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
# [s3_developer]
# aws_access_key_id = AKIA5XNJJZL5QC3Q7IUX
# aws_secret_access_key = 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
# ====================================================================
# Custom Session:

import boto3


# aws_mag_con=boto3.session.Session()

# aws_con_re=aws_mag_con.resource(service_name='ec2',region_name="us-west-2")
# iam_con_client=aws_mag_con.client(service_name='ec2',region_name="us-west-2")

#  print(dir(aws_con_re))



#===============================================================================
#
#
#import boto3
#aws_mag_con=boto3.session.Session(profile_name="root")

#ec2 = aws_mag_con.resource('ec2')

#
# import boto3
# aws_mag_con=boto3.session.Session()


# iam_con_re=aws_mag_con.resource(service_name='iam')#,region_name="us-east-2")
# # iam_con_client=aws_mag_con.client(service_name='iam',region_name="us-east-2")

# for each_user in iam_con_re.roles.all():
#     print(each_user.name)

