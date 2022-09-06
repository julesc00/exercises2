import boto3

"""
boto3.client()
    - this is the original boto3 API abstraction
    - it provides low-level AWS service access
    - all AWS service operations are supported by clients
    - it exposes botocore client to the developer
    - it typically maps 1:1 with the AWS service API
    - it exposes snake-cased method names (e.g. ListBuckets API => list_buckets method)
    - requires you to code result pagination
    - it is generated from an AWS service description
"""


def get_s3_bucket():
    client = boto3.client("s3")
    response = client.list_objects_v2(Bucket="bucket_name")
    for content in response.get("content"):
        obj_dict = client.get_object(Bucket="bucket_name", Key=content.get("Key"))
        print(content.get("Key"), obj_dict.get("LastModified"))
