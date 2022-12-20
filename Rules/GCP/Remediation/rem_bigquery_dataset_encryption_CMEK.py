# Python script that demonstrates how to enable encryption at rest with default Customer-Managed Encryption Keys (CMEKs) for your BigQuery datasets

# Imports the Google Cloud Client Library
from google.cloud import bigquery

# Instantiates a client
client = bigquery.Client()

# The name of the dataset to update
dataset_name = 'my_dataset'

# Retrieve the dataset
dataset = client.get_dataset(dataset_name)

# Set the default encryption configuration to use CMEK
encryption_config = bigquery.EncryptionConfiguration(kms_key_name='projects/my-project/locations/us/keyRings/my-key-ring/cryptoKeys/my-key')
dataset.encryption_configuration = encryption_config

# Update the dataset
dataset = client.update_dataset(dataset, ['encryption_configuration'])

print(f'Encryption at rest is now enabled for dataset {dataset.full_dataset_id} with CMEK.')

# This script assumes that you have already created a Customer-Managed Encryption Key (CMEK) in Cloud KMS and have the key's fully qualified resource name. You will need to replace 'projects/my-project/locations/us/keyRings/my-key-ring/cryptoKeys/my-key' with the actual resource name of your CMEK.
# You will also need to install the Google Cloud Client Library and authenticate the script to access your Google Cloud resources.
