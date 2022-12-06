#how to upload a single file to an s3 bucket using boto3 and python
import boto3
s3_resourse=boto3.client("s3")
s3_resourse.upload_file(
    Filename="<filename.png>"
    Bucket= "<bucketname>"
    key="uploadtest.png")
    

    
#how to upload multiple files to s3 bucket
import os
import glob
cwd=os.getcwd()
cwd=cwd+"/upload/"
files=glob.glob(cwd+"*.png")
files
for file in files:
    s3_resourse=boto3.client("s3")
    s3_resourse.upload_file(
    Filename="<filename.png>"
    Bucket= "<bucketname>"
    key=file.split("/")[])
