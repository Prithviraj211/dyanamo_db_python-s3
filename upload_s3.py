import boto3

s3 = boto3.client('s3')
s3.upload_file('test.txt','s3-program-py','s3_script.text')
print("Done")