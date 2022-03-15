import boto3
import os

ACCESS_KEY=os.getenv('ACCESS_KEY')
ACCESS_ID=os.getenv('ACCESS_ID')
BUCKET=os.getenv('BUCKET')

s3_client = boto3.client('s3', aws_access_key_id=ACCESS_ID, aws_secret_access_key=ACCESS_KEY)

s3_client.upload_file('DADOS/MICRODADOS_ENEM_2020.csv', BUCKET, 'raw-data/MICRODADOS_ENEM_2020.csv')