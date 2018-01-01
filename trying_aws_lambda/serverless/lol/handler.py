import json
import requests
import pandas as pd

def hello(event, context):
    """
    hello function
    """
    data = requests.get("https://www.google.com")
    print data.status_code
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": "testing this out",
        "status_code": data.status_code
    }
    # Testing out pandas
    names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
    births = [968, 155, 77, 578, 973]
    baby_data_set = list(zip(names, births))
    print baby_data_set
    baby_data = pd.DataFrame(data=baby_data_set, columns=['Names', 'Births'])
    print "Printing out the dataframe"
    print baby_data

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
