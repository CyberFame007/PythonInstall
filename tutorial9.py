# How to remove VPC

import boto3

client=boto3.client("ec2")

response = client.delete_vpc(VpcId='vpc-0526fd28b0a01ff19')

print(response)