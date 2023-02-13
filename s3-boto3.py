# Creating an S3 Bucket Using Boto3
import boto3
aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("mychanelpythonbuck3t")
response = bucket.create(
    ACL = 'public-read',
    CreateBucketConfiguration={
        'LocationConstraint':'eu-central-1'
    },
)

print(response)
