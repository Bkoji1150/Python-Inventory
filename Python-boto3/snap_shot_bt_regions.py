import os,sys,botocore
try:
    import boto3
    print("Imported boto3 successfully")
except Exception as e:
    print(e)
    sys.exit(1)
source_region ="us-west-2"
target_region ='us-east-1'

session=boto3.Session()
ec2_source_client=session.client(service_name='ec2', region_name=source_region)
client_sts=session.client(service_name='sts',region_name='us-west-1')
account_id=client_sts.get_caller_identity().get('Account')
ec2_target=session.client(service_name='ec2', region_name=target_region)
bck_snap=[]
f_bkp={'Name': 'tag:backup', "Values":['yes']}
for each_snap in ec2_source_client.describe_snapshots(OwnerIds=[account_id],Filters=[f_bkp]).get("Snapshots"):
    bck_snap.append(each_snap['SnapshotId'])
print("The snapshot id's to be backed up are:", bck_snap)


for each_source_snap_id in bck_snap:
    print("Taking backup for id of {} into  a {}".format(each_source_snap_id,target_region))
    ec2_target.copy_snapshot(
        Description='For DR reason',
        SourceRegion=source_region,
        SourceSnapshotId=each_source_snap_id
    )
print("EBS snapshot copy to destination region is completed")
print("modifying tags for the snapshots for which backup is completed")
for each_source_sna in bck_snap:
    print("Deleting old tags...")
    ec2_source_client.delete_tags(
        Resources=[each_source_sna],
        Tags=[{'Key': 'backup','Value': 'yes'}]
    )
    print(f"creating new tag for: {each_source_sna}")
    ec2_source_client.create_tags(
        Resources=[each_source_sna],
        Tags=[{'Key': 'backup','Value': 'completed'}]
    )

