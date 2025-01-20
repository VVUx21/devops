import boto3
import os
from dotenv import load_dotenv
load_dotenv()
ACCESS_KEY = os.getenv('ACCESS_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')
# Let's use Amazon S3
s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Create a new bucket
s3.create_bucket(Bucket='my-bucket-name')

# Upload a new object
data = open('names.txt', 'rb')
s3.Bucket('my-bucket-name').put_object(Key='test.jpg', Body=data)

# Download an object
s3.Bucket('my-bucket-name').download_file('test.jpg', 'test.jpg')

# Delete a bucket
s3.Bucket('my-bucket-name').delete()

#gettin the parameters from paramsstore
ssm = boto3.client('ssm', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name='eu-north-1')

response = ssm.get_parameter(
    Name='text',
    WithDecryption=True
)
print(response['Parameter']['Value'])

#public urls for s3 bucket
s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
response = s3.generate_presigned_url('get_object', Params={'Bucket': 'my-bucket-name', 'Key': 'test.jpg'}, ExpiresIn=3600)
print(response)
