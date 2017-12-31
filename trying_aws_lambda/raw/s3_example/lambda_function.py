from __future__ import print_function

import json
import requests
import pandas as pd
import os

# Comes with AWS Lambda
import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Testing out triggers with AWS S3
    for record in event['Records']:
        key = record['s3']['object']['key']
        bucket = record['s3']['bucket']['name']
        print(key)
        print(bucket)

    download_path = "/tmp/temp.csv"

    s3_client.download_file(bucket, key, download_path)
    print(os.path.isfile("/tmp/lol.csv"))
    print(os.path.isfile(download_path))

    df2 = pd.read_csv("/tmp/temp.csv")
    print(df2)

    print(sum(df2['col1']))

    return "success"
