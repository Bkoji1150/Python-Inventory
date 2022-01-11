import os
import boto3
from pprint import  pprint

class Ec2(object):

    def __init__(self,instance_status, *instance_id):
        try:
            self.instance_status = instance_status
            self.instance_id = instance_id
            print(
                f'The instance id are {self.instance_id}\nAnd the instance status show {self.instance_status} ')
        except Exception as E:
            print(E)
        return None

    def instance_ids(self):
        try:
            print(f"Your instance ids are {self.instance_id}")

        except Exception as e:
            print(e)
            return None

    def instance_status(self,stopped,running):
        try:
            t = []
            self.stoppped= stopped
            self.running= running
            t.append(self.stoppped)
            print('Your instance status shows',self.stoppped)
        except Exception as e:
            print(e)
            return None

    def Stop_instances(self,message):
        try:
            self.message = message
            print(f'sending {message} to slack that')
        except Exception as e:
            print('e')
            return None

    def Start_instances(self):
        try:
            print(f'python is starting your instances')
        except Exception as e:
            print('e')
            return None

    def Terminating_Instances(self):
        try:
            print('Terminating your instances')
        except Exception as e:
            print(e)
            return None

    def Sendingslack(self):
        try:
            print(f'python is stopping your instances')
        except Exception as e:
            print('e')
            return None

def main():
    try:
        _status = ''
        time = '23444'
        print('Running your ec2 function...')
        List_of_instances = ['s41425253636367', '71625243435353', '62652534343535']
        ec2 = Ec2(List_of_instances,_status)
        ec2.instance_status()
    except Exception as E:
        print(E)
        return None


if __name__ == '__main__':
    main()





