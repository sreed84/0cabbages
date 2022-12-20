# Python script that uses the Google Cloud Client Library for Python (google-auth and google-api-python-client) to determine if your Google Cloud BigQuery dataset tables are encrypted with Customer-Managed Keys (CMKs)

import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Replace this with your project ID
project_id = "your-project-id"

# Authenticate and create a BigQuery client
credentials, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/bigquery"])
bigquery_client = build("bigquery", "v2", credentials=credentials)

# List all of the datasets in your project
response = bigquery_client.datasets().list(projectId=project_id).execute()
datasets = response["datasets"]

# Iterate over the datasets
for dataset in datasets:
    # List all of the tables in the dataset
    tables_response = bigquery_client.tables().list(projectId=project_id, datasetId=dataset["datasetReference"]["datasetId"]).execute()
    tables = tables_response["tables"]

    # Iterate over the tables
    for table in tables:
        # Check if the table is encrypted with a CMK
        if table["encryptionConfiguration"] is not None and table["encryptionConfiguration"]["kmsKeyName"].startswith("projects/your-project-id/locations/global/keyRings/your-key-ring-name/cryptoKeys/your-key-name"):
            print(f"Table {table['tableReference']['tableId']} in dataset {dataset['datasetReference']['datasetId']} is encrypted with a CMK")
# This script lists all of the datasets and tables in your project, and then checks if any of the tables are encrypted with a CMK by checking the encryption configuration for each table. If a table is encrypted with a CMK, it prints the table ID and dataset ID.
# You will need to have the Google Cloud Client Library for Python (google-auth and google-api-python-client) installed and configured on your machine in order to run this script. You can install these libraries using pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client. You will also need to have a Google Cloud account and a project with the BigQuery API enabled, and you will need to set up a service account and download the private key file in order to authenticate with the API. You can find more information on how to do this in the Google Cloud documentation.
# Note: In the script, you will need to replace your-project-id, your-key-ring-name, and your-key-name with the actual values for your project, key ring, and key. You can find these values in the Google Cloud Console.
