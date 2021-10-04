import boto3
from variables import db_password
import psycopg2
import pprint
import botocore
session=boto3.session.Session()
client=session.client(service_name='rds',region_name='us-west-2')
db_id='database-for-hqr-microservices-bck'
try:
    response= client.create_db_instance(
        DBName='Postgres',
        DBInstanceIdentifier=db_id,
        AllocatedStorage=20,
        DBInstanceClass='db.t2.medium',
        EngineVersion='11.9',
        Engine='postgres',
        MasterUsername='hqrdemo',
        PubliclyAccessible=True,
        MasterUserPassword=db_password
    )
    id=response.DBInstanceIdentifier
except Exception as e:
    print(e)
print(f"Creating {id} instance...")
waiter = client.get_waiter('db_instance_available')
waiter.wait(DBInstanceIdentifier=db_id)
print(f"{id} successfull created")

res_id = client.describe_db_instances(DBInstanceIdentifier=db_id)
for each_instance_id in res_id['DBInstances']:
    db_name=each_instance_id.get('DBName')
    db_host= each_instance_id.get('Endpoint')['Address']
    db_user=each_instance_id.get('MasterUsername')

print(f"The db_name is: {db_name}\n The host is: {db_host}\n The pass_w: {db_password}")


# Start a connection
# conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pass, host=db_host)
#
# # create a client cursor
# cur= conn.cursor()
# list_of_schema=[]
#
# # cursor to run your
# cur.execute("SELECT ")
# for schema in cur.fetchall():
#     list_of_schema.append(schema)
# print(list_of_schema)
# # cur.execute("iNSERT INTO student(name) VALUES(%s)", ('bello',))
# #
# # cur.execute('SELECT name from student where id= 1;')
# # print(cur.fetchall())
# # conn.commit()
#
# cur.close()
# conn.close()
