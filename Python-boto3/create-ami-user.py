



import boto3

def get_iam_client_object():
    session=boto3.session.Session()
    iam_client=session.client(service_name="iam")
    return iam_client

def get_random_passwd():
    len_of_password=8
    valid_passwd="qedanwkaqsrfdxzcvghtrewqw@!~`!2_+_,<''>y98785y34566\AX;RVZMdcla"
    password=[]
    for each_char in range(len_of_password):
        password.append(choice(valid_passwd))
        random_passwd=("".join(password))
        print(random_passwd)
        policyArn="arn:aws:iam::aws:policy/AdministratorAccess"
        iam_client.create_user(username=iam_user_name,password=password,passwordResetRequired=False)
        iam_client.attach_user_policy(user_name=iam_user_name,policyArn=policyArn)
        # print "IAM USER Name={} and password={}".format(iam_user_name,random_passwd)
        return None
def mai_iam():
    iam_client=get_aim_cleitn_object()
    iam_user_name="hgdhyeygfhjksheue"
