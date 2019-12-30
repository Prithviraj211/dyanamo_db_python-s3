import boto3
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('users')

table.put_item(
        Item={
                'username':'prithvi',
                'Firstname':'Raj',
                 'lastname':'singh',
                'age':25
}
)
