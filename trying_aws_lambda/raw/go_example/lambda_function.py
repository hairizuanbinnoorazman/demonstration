from __future__ import print_function

import json
import subprocess

def lambda_handler(event, context):
    value = subprocess.check_output("./main", shell=True)
    print(value)
    
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "*/*"
        }
    }    
    return response
