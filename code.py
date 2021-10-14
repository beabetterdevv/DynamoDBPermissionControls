import boto3
from boto3.dynamodb.conditions import Key
import constants

client = boto3.resource('dynamodb',
    aws_access_key_id = constants.aws_access_key_id,
    aws_secret_access_key = constants.aws_secret_access_key
)

table = client.Table("CustomerOrders")

response = table.query(
        ProjectionExpression="CustomerID, OrderID, CommonAttribute_OrderTotal",
        KeyConditionExpression=Key('CustomerID').eq('CUSTOMER1')
	)

print(response['Items'])