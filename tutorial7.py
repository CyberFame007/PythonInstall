# Creating a VPC using boto3 python

import boto3
client=boto3.client("ec2")
response = client.create_vpc(CidrBlock='10.20.0.0/16')

print(response)
