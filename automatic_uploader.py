from configure import access_key, secret_access_key

import boto3
import os

client = boto3.client('s3',
                      aws_access_key_id=access_key,
                      aws_secret_access_key=secret_access_key)


for file in os.listdir():
    if '.py' in file:
        upload_file_bucket = 'bmooneytestbucket'
        upload_file_key = 'python/' + str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)
    if '.js' in file:
        upload_file_bucket = 'bmooneytestbucket'
        upload_file_key = 'javascript/' + str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)
    if '.java' in file:
        upload_file_bucket = 'bmooneytestbucket'
        upload_file_key = 'java/' + str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)
    if '.html' in file:
        upload_file_bucket = 'bmooneytestbucket'
        upload_file_key = 'html/' + str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)
    if '.css' in file:
        upload_file_bucket = 'bmooneytestbucket'
        upload_file_key = 'css/' + str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)
    if '.php' in file:
        upload_file_bucket = 'bmooneytestbucket'
        upload_file_key = 'php/' + str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)
