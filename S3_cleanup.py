import boto3

def clean_up(session, aws_s3_bucket, aws_s3_path):
    s3 = session.resource('s3')
    bucket = s3.Bucket(aws_s3_bucket)
    for obj in bucket.objects.filter(Prefix=aws_s3_path):
        s3.Object(bucket.name,obj.key).delete()