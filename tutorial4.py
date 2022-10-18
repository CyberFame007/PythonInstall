# How To Set Policy For Aws S3 Bucket Using Boto3 Python

import boto3
import json


s3_resource=boto3.client("s3")
s3_resource.put_bucket_policy(Bucket="pyfame1011private",Policy=bucket_policy)



bucket_policy={
  "Id": "Policy1665714941786",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1665712442534",
      "Action": [
        "s3:GetObject"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::pyfame1011private/*",
      "Principal": "*"
    }
  ]
}


bucket_policy=json.dumps(bucket_policy)

#copy1