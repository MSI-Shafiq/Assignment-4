import boto3;

class DynamoDBExample:
    
    items = [
        {
            'id': 1,
            'name': 'item1',
            'price': 23,
            'stock': 50
        },
        {
            'id': 2,
            'name': 'item2',
            'price': 10,
            'stock': 100
        },
        {
            'id': 3,
            'name': 'item3',
            'price': 20,
            'stock': 150
        }
    ]
    
    def createTable(self, dynamodb=None):
        if not dynamodb:
            dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
        
        table = dynamodb.Table('INVENTORY')
        
        if not table:
            table = dynamodb.create_table(
                TableName='INVENTORY',
                KeySchema=[
                    {
                        'AttributeName': 'id',
                        'KeyType': 'HASH'  
                    },
                    {
                        'AttributeName': 'name',
                        'KeyType': 'RANGE'  
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'id',
                        'AttributeType': 'N'
                    },
                    {
                        'AttributeName': 'name',
                        'AttributeType': 'S'
                    }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 4,
                    'WriteCapacityUnits': 4
                }
            )
        return table
    
    def insertData(self, dynamodb=None):
        if not dynamodb:
            dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
            
        table = dynamodb.Table('INVENTORY')
        for item in self.items:
            table.put_item(Item=item)
            
    def selectData(self, dynamodb=None):
        if not dynamodb:
            dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
            
        table = dynamodb.Table('INVENTORY')
        retrieved_items = table.scan()
        
        print(retrieved_items)
        
        
        
dynamoDbExample = DynamoDBExample()
inventory_table = dynamoDbExample.createTable()
print("Table status:", inventory_table.table_status)
dynamoDbExample.insertData()
dynamoDbExample.selectData()
