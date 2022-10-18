# How to create EBS volume using boto3 python

import boto3

ec2_client=boto3.client("ec2")

response=ec2_client.create_volume(
    AvailabilityZone='us-east-1a',
    Size=8,
    Encrypted=True,
    VolumeType='gp2',
    TagSpecifications=[
        
        {
            'ResourceType': 'volume',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'tutorial14a'
                },
                
            ]
        
        },
    
    ]
    
)

print(response)