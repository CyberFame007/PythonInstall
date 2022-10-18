# How to create ec2 instance with python

import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId='ami-026b57f3c383c2eec',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    SubnetId='subnet-075f4f7b20324725c'
)
print(instance)