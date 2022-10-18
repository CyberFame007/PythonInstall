# How to create multiple ec2 using boto3 python

import boto3

ec2_resource=boto3.resource("ec2")

x=ec2_resource.create_instances(
    ImageId='ami-026b57f3c383c2eec',
    MinCount=3,
    MaxCount=3,
    InstanceType='t2.micro',
    SubnetId='subnet-075f4f7b20324725c'
)

print(x)