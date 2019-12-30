import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(TableName= "users",
                               KeySchema=[{
                                            'AttributeName':'username',
                                            'KeyType': 'HASH'},
                                   {
                                            'AttributeName':'lastname',
                                            'KeyType': 'RANGE'
                                   }
                            ],
AttributeDefinitions=[
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
       {
            'AttributeName': 'lastname',
            'AttributeType': 'S'
        }],

        ProvisionedThroughput={
                                'ReadCapacityUnits': 5,
                                'WriteCapacityUnits': 5
                              })

table.meta.client.get_waiter('table_exists').wait(TableName='users')

print(table.item_count)