# Queriying data from S3 using AWS Athena and Boto3
Simple way to query Amazon Athena in python with boto3

**STARS** and **FORKS** keep me motivated to do more work.

### You can follow this blog link:  
https://medium.com/dataseries/auto**mating-athena-queries-from-s3-with-python-and-save-it-as-csv-8917258b1045


---
forked on 29 apr 2021 from https://github.com/raoofnaushad/AWSathena_s3_python
---


I have some update it. 

boto3.resource doesn't get session information So, directly input the session info. 
And Some information have to manualy in S3_cleanup.py file. it's get from parmas value. 
likely 'bucket', 'prefix'


You have to put in parmas value with yours

```
params = {
    'region': "INPUT Your Region"
    'database': "INPUT Your Athena Database",
    'bucket': "INPUT Your S3 Bucket Name"
    'path': "INPUT Your S3 PATH "
    'query': "INPUT Your SQL Query in Athena"
}
```