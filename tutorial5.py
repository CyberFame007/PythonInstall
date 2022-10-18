# How To Get Policy For Aws S3 Bucket Using Boto3 Python



import boto3


s3_resource=boto3.client("s3")
s3_resource.get_bucket_policy(Bucket="pyfame1011private")