# Python script that uses the Google Cloud Client Library for Python (google-auth and google-api-python-client) to determine if your Google Cloud BigQuery datasets are encrypted using default Customer-Managed Encryption Keys (CMEKs)

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
    # Get the dataset's encryption configuration
    encryption_config = bigquery_client.datasets().get(projectId=project_id, datasetId=dataset["datasetReference"]["datasetId"]).execute()["encryptionConfiguration"]

    # Check if the dataset is encrypted using a default CMEK
    if encryption_config is not None and encryption_config.get("kmsKeyName", "").startswith("projects/cloud-sql-cloud-key-ring/cryptoKeys/cloud-key"):
        print(f"Dataset {dataset['datasetReference']['datasetId']} is encrypted using a default CMEK")
# This script lists all of the datasets in your project, and then checks if any of them are encrypted using a default CMEK by checking the encryption configuration for each dataset. If a dataset is encrypted using a default CMEK, it prints the dataset ID.
# You will need to have the Google Cloud Client Library for Python (google-auth and google-api-python-client) installed and configured on your machine in order to run this script. You can install these libraries using pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client. You will also need to have a Google Cloud account and a project with the BigQuery API enabled, and you will need to set up a service account and download the private key file in order to authenticate with the API. You can find more information on how to do this in the Google Cloud documentation.
