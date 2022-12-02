import boto3
resource=boto3.resource("s3")
bucket_list=list(resource.buckets.all())
len(bucket_list)
for bucket in resource.bucket.all():
    print(bucket.name)