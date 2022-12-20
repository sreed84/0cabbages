# Python script that uses the Google Cloud Client Library for Python (google-auth and google-api-python-client) to enable encryption with Cloud KMS Customer-Managed Keys (CMKs) for your BigQuery dataset tables

import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build

# Replace these values with your own
project_id = "your-project-id"
dataset_id = "your-dataset-id"
table_id = "your-table-id"
key_ring_name = "your-key-ring-name"
key_name = "your-key-name"

# Authenticate and create a BigQuery client
credentials, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/bigquery"])
bigquery_client = build("bigquery", "v2", credentials=credentials)

# Construct the encryption configuration for the table
encryption_config = {
    "kmsKeyName": f"projects/{project_id}/locations/global/keyRings/{key_ring_name}/cryptoKeys/{key_name}"
}

# Update the table to use the CMK for encryption
try:
    bigquery_client.tables().patch(
        projectId=project_id,
        datasetId=dataset_id,
        tableId=table_id,
        body={
            "encryptionConfiguration": encryption_config
        }
    ).execute()
    print("Successfully enabled encryption with CMK for table")
except HttpError as error:
    print(f"Failed to enable encryption with CMK for table: {error}")
# This script updates the encryption configuration for a specific table in a BigQuery dataset to use a CMK for encryption. It sets the kmsKeyName field in the encryption configuration to the fully qualified name of the CMK.
# You will need to have the Google Cloud Client Library for Python (google-auth and google-api-python-client) installed and configured on your machine in order to run this script. You can install these libraries using pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client. You will also need to have a Google Cloud account and a project with the BigQuery API enabled, and you will need to set up a service account and download the private key file in order to authenticate with the API. You can find more information on how to do this in the Google Cloud documentation.
# Note: In the script, you will need to replace your-project-id, your-dataset-id, your-table-id, your-key-ring-name, and your-key-name with the actual values for your project, dataset, table, key ring, and key. You can find these values in the Google Cloud Console.
