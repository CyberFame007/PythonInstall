# creating an S3 bucket with python code
import boto3
aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("pyfame1private")
response = bucket.create(
    ACL='private',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    },

)   

print(response)