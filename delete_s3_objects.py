#delete single object from s3 bucket
import boto3
s3_resource=boto3.client("s3")
s3_resource.delete_object(Bucket='nameofbucket',
    Key='filename.png')
    
#delete multiple objects
import os
import glob
#find all objects from bucket
s3_resource.list_objects(Bucket="bucketname") ["Contents"]
len(objects)
#find name of files 
for object in objects:
    response=s3_resource.list_objects(Bucket="bucketname",
     Key=object["Key"])
    print (response)