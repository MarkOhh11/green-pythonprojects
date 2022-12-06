#how to list objects from an s3 bucket
import boto3
s3_resource=boto3.client("s3")
s3_resource.list_objects(Bucket="bucketname")["Contents"]
len(objects)
if len(objects)>0:
    print("objects exist")
    
for object in objects:
    print(object["Key"]) #'Key' will be the file name
