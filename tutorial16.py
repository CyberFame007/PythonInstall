# How to delete EBS volume using boto3 python

import boto3
ec2_client=boto3.client("ec2")
response=ec2_client.delete_volume(VolumeId= 'vol-08b904f6da40a2ed7')

print(response)
