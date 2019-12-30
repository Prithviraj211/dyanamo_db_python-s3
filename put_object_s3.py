import boto3

from botocore.client import Config

ACCESS_KEY_ID = 'AKIAIQA4B53G7MWAXULA'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 's3-program-py'

data = open('test.png', 'rb')

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)

s3.Bucket(BUCKET_NAME).put_object(Key='test.png', Body=data, ACL='public-read')

print("Done")

