import psycopg2

db_name="dbabello"
db_host="postgresdevops.cob6rtnzogmw.us-west-2.rds.amazonaws.com"
db_user="dbabello"
db_pass="brontech1"

conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pass, host=db_host)
cur= conn.cursor()

# cur.execute("CREATE TABLE student (id SERIAL PRIMARY KEY, name varchar);")
# cur.execute("iNSERT INTO student(name) VALUES(%s)", ('bello',))

cur.execute('SELECT name from student where id= 1;')
print(cur.fetchall())
conn.commit()

cur.close()
conn.close()
