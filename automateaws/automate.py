import boto3

session = boto3.Session(profile_name='pythonauto')

s3 = session.resource('s3')

for bucket in s3.buckets.all():
  print(bucket)





if __name__ = '__main__':
 print("Hello, world")
