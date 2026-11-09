"""AWS Lambda power-calculator handler, reconstructed from the project notes.

Accepts API Gateway proxy events with a JSON body containing integer base and
exponent values; returns the result as a JSON number.
"""
import json
import math


def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        base = int(body['base'])
        exponent = int(body['exponent'])
        result = math.pow(base, exponent)

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps(result)
        }
    except Exception as e:
        # Preserve the original tutorial-project behavior; a future improvement
        # would distinguish invalid input (HTTP 400) from server errors.
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(str(e))
        }
