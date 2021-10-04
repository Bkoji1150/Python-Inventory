import os,sys,botocore
try:
    import boto3
    print("Imported boto3 successfully")
except Exception as e:
    print(e)
    sys.exit(1)

def lambda_handler(event, context):
    source_region ="us-west-2"
    target_region ="us-east-1"
    ec2_target = boto3.client(service_name='ec2', region_name=target_region)

    ec2_source_client=boto3.client(service_name='ec2', region_name=source_region)
    client_sts=boto3.client(service_name='sts',region_name='us-west-1')
    ec2_target=boto3.client(service_name='ec2', region_name=target_region)
    bck_snap=[]
    f_bkp={'Name': 'tag:backup', "Values":['yes']}
    for each_snap in ec2_source_client.describe_snapshots(Filters=[f_bkp]).get("Snapshots"):
        bck_snap.append(each_snap['SnapshotId'])
        for each_source_snap_id in bck_snap:
            ec2_target.copy_snapshot(
                Description='For DR reason',
                SourceRegion=source_region,
                SourceSnapshotId=each_source_snap_id
                )
    for each_source_sna in bck_snap:
        ec2_source_client.delete_tags(
            Resources=[each_source_sna],
            Tags=[{'Key': 'backup','Value': 'yes'}]
            )
        ec2_source_client.create_tags(
            Resources=[each_source_sna],
            Tags=[{'Key': 'backup','Value': 'completed'}]
            )