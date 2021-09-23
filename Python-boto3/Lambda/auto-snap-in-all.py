import sys

import boto3

sesion=boto3.session.Session()
aws_con_re=sesion.resource(service_name="ec2", region_name="us-west-2")
aws_con_client = sesion.client(service_name="ec2", region_name="us-west-2")

all_regions = []
vol_ids=[]
snap_ids = []

for each_region in aws_con_client.describe_regions()['Regions']:
    all_regions.append(each_region['RegionName'])
    print('working on..: ', all_regions)
for each_vol in aws_con_re.volumes.filter(Filters=[]):
    vol_ids.append(each_vol.id)
    print(f'The volume ids are...: ',vol_ids)
for each_vo_id in vol_ids:
    a=aws_con_re.create_snapshot(
        Description='Snap with Lambda',
        VolumeId=each_vo_id,
        TagSpecifications=[
            {
                'ResourceType': 'snapshot',
                'Tags': [
                    {
                        'Key': 'Delete-on',
                        'Value': '90'
                    }
                ]
            }
        ]
    )
snap_ids.append(a.id)
print(snap_ids)
# Creating waiter using client
print('taken snapshots...')
waiter = aws_con_client.get_waiter('snapshot_completed')
waiter.wait(SnapshotIds=snap_ids)
print("snap show completed")



