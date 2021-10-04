import sys

import boto3
import pprint
import sys

session=boto3.session.Session()
client=session.client(service_name='rds',region_name='us-west-2')
# #
# for db_instances in client.describe_db_instances()["DBInstances"]:
#     hqr_id=db_instances.get('DBInstanceIdentifier')
#     if db_instances.get('DBInstanceStatus')=="available":
#         print("The instance would be stopping..!")
#         client.stop_db_instance(DBInstanceIdentifier=hqr_id)
#         print("The instance is stopped..!")
#     else:
#         print("Nothing to do")
#         sys.exit()
#
# strftime("%Y-%m-%d %H:%M:%S")
# sn_ids=[]
# sn_time=[]
# count=1
# for snapshot in client.describe_db_snapshots()['DBSnapshots']:
#     sn_ids.append(snapshot['DBSnapshotIdentifier'])
#     sn_time.append(snapshot.get('SnapshotCreateTime').strftime('%Y-%m-%d %H:%M:%S'))
#     if len(sn_ids)==3:
#         print(sn_ids)
#         for each in sn_ids:
#             print(f"deleting these snapshots {each}")
#             client.delete_db_snapshot(DBSnapshotIdentifier=each)
#             waiter = client.get_waiter('db_snapshot_deleted')
#             waiter.wait(DBSnapshotIdentifier=each)
#             print("Snapshot delete completed...!!!")
#             sys.exit(1)

# Delete rds instance ...!!

for db_instances in client.describe_db_instances()["DBInstances"]:
    b=db_instances['DBInstanceIdentifier']
    print(b)
client.delete_db_instance(
    DBInstanceIdentifier=b)
waiter = client.get_waiter('db_instance_deleted')
waiter.wait(DBInstanceIdentifier=b)


