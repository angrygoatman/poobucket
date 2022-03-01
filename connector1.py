import boto3
import pandas as pd
import os


s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-1',
    aws_access_key_id='access key',
    aws_secret_access_key='secret key'
)




for bucket in s3.buckets.all():
    print(bucket.name)

    
# Make dataframes
foo = pd.DataFrame({'x': [1, 2, 3], 'y': ['a', 'b', 'c']})
bar = pd.DataFrame({'x': [10, 20, 30], 'y': ['aa', 'bb', 'cc']})

# Save to csv
foo.to_csv('foo.csv')
bar.to_csv('bar.csv')

s3.Bucket('poobucket2357').upload_file(Filename='foo.csv', Key='foo.csv')
s3.Bucket('poobucket2357').upload_file(Filename='bar.csv', Key='bar.csv')

for obj in s3.Bucket('poobucket2357').objects.all():
    print(obj)

obj = s3.Bucket('poobucket2357').Object('foo.csv').get()
foo = pd.read_csv(obj['Body'], index_col=0)

print(foo)

obj = s3.Bucket('poobucket2357').Object('bar.csv').get()
bar = pd.read_csv(obj['Body'], index_col=0)

print(bar)


s3.Bucket('poobucket2357').download_file(Key='foo.csv', Filename='foo2.csv')
x = pd.read_csv('foo2.csv', index_col=0)

print(x)



