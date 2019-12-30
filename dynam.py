import boto3

dynamodb = boto3.resource('dynamodb',region_name='ap-south-1', endpoint_url="https://dyanamodb.ap-south-1.amazonaws.com")

table = dynamodb.Table('testing')

response = table.put_item(TableName='testing',
    Item={'ID':1,'Name':"Prithviraj",'Age':22, 'Location':"Indore"}
               )

print(response["ResponseMetadata"]["RetryAttempts"])
print("Done")