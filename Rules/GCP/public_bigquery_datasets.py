# Python script that uses the Google Cloud Client Library for Python (google-auth and google-api-python-client) to determine if there are any publicly accessible BigQuery datasets available within your Google Cloud account

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
    # Check if the dataset is publicly accessible
    if dataset["access"][0]["role"] == "READER" and dataset["access"][0]["specialGroup"] == "allAuthenticatedUsers":
        print(f"Dataset {dataset['datasetReference']['datasetId']} is publicly accessible")

        
# This script lists all of the datasets in your project, and then checks if any of them are publicly accessible by checking the access permissions for each dataset. If a dataset is publicly accessible, it prints the dataset ID.
# You will need to have the Google Cloud Client Library for Python (google-auth and google-api-python-client) installed and configured on your machine in order to run this script. You can install these libraries using pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client. You will also need to have a Google Cloud account and a project with the BigQuery API enabled, and you will need to set up a service account and download the private key file in order to authenticate with the API. You can find more information on how to do this in the Google Cloud documentation.
