import os
import sys
import boto3
import time
from pprint import pprint
import json
aws_con = boto3.session.Session()

# Global Variables

no_prod_ids=[]
instance_ids_ = []
__all_instance_status = []
f1={"Name": "tag:Name", "Values": ['prod']}


def __ec2__():
    try:
        while True:
            import requests
            # Start, Stop, Terminate, Exit ec2 using Boto3 client Sending Slack when Done
            aws_con_re = aws_con.resource(service_name="ec2", region_name="us-west-2")
            aws_con_client = aws_con.client(service_name="ec2", region_name="us-west-2")
            webhook = os.environ.get("webhook_slack")
            for each in aws_con_re.instances.filter(Filters=[f1]):
                no_prod_ids.append(each.id)
                instance_ids_.append(each.state)
            for r in instance_ids_:
                __all_instance_status.append(r.get('Name'))

            # Get all Tags
            list_of_tags = []
            for each in aws_con_re.instances.filter(Filters=[f1]):
                for each_tags in each.tags:
                    list_of_tags.append(each_tags['Value'])

            # Monitor instances
            ids_of = []
            stopped_in = []
            n = 'stopped'
            dictionary = dict(zip(no_prod_ids, __all_instance_status))
            for key, values in dictionary.items():
                if values == n:
                    ids_of.append(key), stopped_in.append(values)
                    _diction = dict(zip(ids_of, stopped_in))
            if stopped_in.count(n) != 0:
                data = {
                    "text": f"""There are {stopped_in.count(n)} occurrences of {n} Instances\nWith instance id of {ids_of}\nAt this Time: {time.strftime("%m-%d-%Y, %H:%M:%S")} """
                    }
                print("Sending A slack Message.")
                requests.post(webhook, json.dumps(data))

            # Hit 1 to Start your instance
            opt = int(input(f"Enter 1. To START Your Innstances:,\nEnter 2 To Stop Your Innstance:,\nEnter 3 To Terminate Your Innstance:,\nEnter 4 To Exit.: "))
            if opt == 1:
                for i_in_stat in __all_instance_status:
                    if 'running' != i_in_stat:
                        print("Instances are starting....")
                        aws_con_client.start_instances(InstanceIds=no_prod_ids)
                        waiter =  aws_con_client.get_waiter('instance_running')
                        waiter.wait(InstanceIds=no_prod_ids)
                        print("Your instance got started...")
                        data = {
                            "text": f"""There are {stopped_in.count(n)} Instances That Got Started\nWith instance id of {ids_of}\nAt this Time: {time.strftime("%m-%d-%Y, %H:%M:%S")} """
                            }
                        print("Sending A slack Message.")
                        requests.post(webhook, json.dumps(data))
                        time.sleep(5)
                        print("Done!!!")
                        sys.exit()
                    else:
                        print(f"Your instances state shows {__all_instance_status}")
                        print('Nothing to do!')
                        sys.exit(1)
            elif opt == 2:
                # Hit 2 to Stop your instance
                # stop_instance = ec2_client.stop_instances(InstanceIds=[ec2_insta_ids])
                    for i_in_stat in __all_instance_status:
                        if i_in_stat == 'running':
                            print("Instances are stopping....")
                            aws_con_client.stop_instances(InstanceIds=no_prod_ids)
                            waiter = aws_con_client.get_waiter('instance_stopped')
                            waiter.wait(InstanceIds=no_prod_ids)
                            print("Your instances are stopped...")
                            # SLack a Message that Instance Got stopped
                            data = {
                                "text": f"""There are {stopped_in.count(n)} Instances That Got Stopped\nWith instance id of {ids_of}\n, At this Time: {time.strftime("%m-%d-%Y, %H:%M:%S")} """
                            }
                            print("Sending A slack Message Instance being stopped.")
                            requests.post(webhook, json.dumps(data))
                            print("Done!!!")
                            sys.exit(1)

                        else:
                            print(f"Your instance state shows {__all_instance_status}")
                            print('Nothing to do!')
                            sys.exit()
            elif opt == 3:
                print("Waring!!! Terminating you Instance ---")
                for i in ('running', 'stopped'):
                    for i_in_stat in __all_instance_status:
                        if i_in_stat == i:
                            print(f"Terminating These {no_prod_ids} Instance....")
                            aws_con_client.terminate_instances(InstanceIds=no_prod_ids)
                            waiter = aws_con_client.get_waiter('instance_terminated')
                            waiter.wait(InstanceIds=no_prod_ids)
                            print("Your instances Just got terminated...")
                            # SLack a Message that Instance Got terminated'
                            data = {
                                "text": f"""There are {stopped_in.count(n)} Instances That Got terminated\nWith instance id of {ids_of}\n, At this Time: {time.strftime("%m-%d-%Y, %H:%M:%S")} """
                            }
                            print("Sending A slack Message Instance being terminated.")
                            requests.post(webhook, json.dumps(data))
                            time.sleep(2)
                            print("Done!!!")
                            sys.exit(1)

                        else:
                            print(f"Your instance state shows: {__all_instance_status}")
                            print('Nothing to do!')
                            sys.exit()
            elif opt==4:
                print("Exiting your Script----")
                sys.exit(1)
            else:
                print("Your Option is Invalid Chose either (1, 2, 3, 4) From the Option")
                sys.exit(5)
    except Exception as e:
            print(e)
    return None


def main():
    __ec2__()
    return None


try:
    if __name__=='__main__':

        main()
except Exception as e:
    print(e)