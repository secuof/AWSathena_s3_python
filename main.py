import boto3
import pandas
import time 
import csv
import athena_from_s3
import S3_cleanup

params = {
    'region': "INPUT Your Region"
    'database': "INPUT Your Athena Database",
    'bucket': "INPUT Your S3 Bucket Name"
    'path': "INPUT Your S3 PATH "
    'query': "INPUT Your SQL Query in Athena"
}

session = boto3.Session(profile_name='INPUT your profile name for AWS Credential')

## Fucntion for obtaining query results and location 
location, data = athena_from_s3.query_results(session, params)
print("Locations: ",location)
print("Result Data: ")
print(data)
## Function for cleaning up the query results to avoid redundant data
S3_cleanup.clean_up(session, params['bucket'], params['path'])