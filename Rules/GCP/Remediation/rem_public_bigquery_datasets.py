# Python script that demonstrates how to remove all "allUsers" and/or "allAuthenticatedUsers" member bindings from the dataset ACLs in order to restrict anonymous and/or public access to your Google Cloud BigQuery datasets

# Imports the Google Cloud Client Library
from google.cloud import bigquery

# Instantiates a client
client = bigquery.Client()

# The name of the dataset
dataset_name = 'my_dataset'

# Retrieve the dataset
dataset = client.get_dataset(dataset_name)

# Get the current ACL for the dataset
acl = dataset.access_entries

# Remove all "allUsers" and "allAuthenticatedUsers" member bindings from the ACL
acl = [entry for entry in acl if entry.entity.type != 'allUsers' and entry.entity.type != 'allAuthenticatedUsers']

# Update the dataset with the modified ACL
dataset.access_entries = acl
dataset = client.update_dataset(dataset, ['access_entries'])

print(f'Removed all "allUsers" and "allAuthenticatedUsers" member bindings from the ACL for dataset {dataset.full_dataset_id}.')

# This script assumes that you have already authenticated the script to access your Google Cloud resources.
