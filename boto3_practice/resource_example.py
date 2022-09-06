import boto3
"""
boto3.resource()
    - this is the newer boto3 API abstraction
    - it provides a high-level, object-oriented API
    - it does not provide 100% API coverage of AWS services
    - it uses identifiers and attributes
    - it has actions (operations on resources)
    - it exposes sub-resources and collections of AWS resources
    - does result pagination for you
    - it is generated from an AWS resource description
"""


def get_s3_bucket():
    s3 = boto3.resource("s3")
    bucket = s3.Bucket("bucket_name")
    for obj in bucket.objects.all():
        print(obj.key, obj.last_modified)
