import boto3
import datetime

aws_con_session=boto3.session.Session()
aws_con_re=aws_con_session.resource(service_name="ec2",region_name="us-west-2")
today=datetime.datetime.now()
start_time=str(datetime.datetime(today.year,today.month,today.day,13,47,43))

print(start_time)
# aws_mag_con_user= boto3.session.Session(profile_name="koji-devops")
# aws_mag_con= boto3.session.Session()
aws_mag_client=aws_con_session.client('sts')

response =aws_mag_client.get_caller_identity()
my_acct_id=response.get('Account')

for each in aws_con_re.snapshots.filter(OwnerIds=[my_acct_id]):
    if each.start_time.strftime("%Y-%m-%d %H:%M:%S")==start_time:
        print (each.id,each.start_time.strftime("%Y-%m-%d %H:%M:%S"))

# filter_size={"Name": "volume-size", "Values": ['10']}
#
# print("Snapshots that are greater than 10GiBs")
# for each_snap in aws_con_re.snapshots.filter(OwnerIds=[my_acct_id],Filters=[filter_size]):
#         print(each_snap.id)




'''
List all snapshots based on size!
'''


'''
docker_container.nodered_container.ip_address
https://www.google.com/search?q=force+user+to+change+password+at+next+logon+postgres&rlz=1C1CHBD_enUS877US877&oq=&aqs=chrome.3.69i59i450l8.4683j0j7&sourceid=chrome&ie=UTF-8
'''