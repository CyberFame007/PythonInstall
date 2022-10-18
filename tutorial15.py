# How to describe EBS volume using boto3 python

import boto3

ec2=boto3.client("ec2")

response=ec2.describe_volumes()

data=response["Volumes"]

print(data)