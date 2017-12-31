from __future__ import print_function

import json
import requests

def lambda_handler(event, context):
    response = requests.get("https://www.google.com")
    print("Print the status code of this")
    print(response.status_code)
    
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "*/*"
        }
    }    
    return response
