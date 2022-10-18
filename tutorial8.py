# How to describe VPC using python

import boto3

client=boto3.client("ec2")

# How to describe all VPC available in your account

x=client.describe_vpcs()

no_of_vpcs=x["Vpcs"]
len(no_of_vpcs)

for vpc in no_of_vpcs:
    print(vpc["VpcId"])
    

    
y=client.describe_vpcs(VpcIds=["vpc-00b5161c83722e8c0"])    

print(y)
    



