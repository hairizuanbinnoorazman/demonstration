from __future__ import print_function

import json
import requests
import pandas as pd

def lambda_handler(event, context):
    # Testing out pandas
    names = ['Bob','Jessica','Mary','John','Mel']
    births = [968, 155, 77, 578, 973]
    BabyDataSet = list(zip(names,births))
    print(BabyDataSet)
    df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
    print("Printing out the dataframe")
    print(df)  
     
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "*/*"
        }
    }    
    return response
