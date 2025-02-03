import json
import boto3
import string
import random

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('URLShortener')

def generate_short_code():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

def lambda_handler(event, context):
    http_method = event['httpMethod']
    
    if http_method == 'POST':
        # Create a short URL
        body = json.loads(event['body'])
        long_url = body['long_url']
        short_code = generate_short_code()
        
        table.put_item(Item={
            'short_code': short_code,
            'long_url': long_url
        })
        
        return {
            'statusCode': 200,
            'body': json.dumps({'short_code': short_code})
        }
    
    elif http_method == 'GET':
        # Redirect to the long URL
        short_code = event['queryStringParameters']['short_code']
        response = table.get_item(Key={'short_code': short_code})
        
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Short URL not found'})
            }
        
        long_url = response['Item']['long_url']
        return {
            'statusCode': 301,
            'headers': {'Location': long_url}
        }
    
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid HTTP method'})
        }
