import boto3

session = boto3.Session()
creds = session.get_credentials()

print("AWS Access Key:", creds.access_key if creds else "NOT FOUND")
print("Region:", session.region_name)
