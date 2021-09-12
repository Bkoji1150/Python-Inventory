#!/bin/python
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='ec2-52-33-193-35.us-west-2.compute.amazonaws.com',username='paramiko',password='koji',port=22)
# ssh.connect(hostname='ec2-52-33-193-35.us-west-2.compute.amazonaws.com',username='ec2-user',key_filename='C:\\Users\\new\\Downloads\\jenkins-keypair.pem',port=22)
# stdin, stdout, stderr = ssh.exec_command('free -m')
sftp_client=ssh.open_sftp()
# sftp_client.chdir("/home/paramiko")
# print(sftp_client.getcwd())
# sftp_client.get('/home/paramiko/love.sh','C:\\Users\\new\\Documents\\love_downloaded.sh')
sftp_client.put('ec2-startInstance.py','/home/paramiko/ec2-startInstance.py')
sftp_client.close()
ssh.close()

#stdin, stdout, stderr = ssh.exec_command('uptime')
# stdin, stdout, stderr = ssh.exec_command('free -m')
# print("The output is: ")
# print(stdout.readlines())
