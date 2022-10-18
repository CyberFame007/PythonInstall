# How to terminate multiple ec2 using boto3 python

import boto3

ec2_client=boto3.client('ec2')

x=ec2_client.describe_instances()

data=x["Reservations"]

li=[]
for instances in data:
    instances=instances["Instances"]
    for ids in instances:
        instance_id=ids["InstanceId"]
        print(instance_id)
        li.append(instance_id)
        
        
response=ec2_client.terminate_instances(InstanceIds=li)   

print(response)
        