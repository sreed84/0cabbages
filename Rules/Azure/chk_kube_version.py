# Python script that uses the Azure Python SDK (azure-mgmt-containerservice) to determine if your Azure Kubernetes Service (AKS) clusters are using the latest available version of Kubernetes


import json
import re
import requests

from azure.mgmt.containerservice import ContainerServiceClient
from azure.common.credentials import ServicePrincipalCredentials

# Replace these values with your own
client_id = "your-client-id"
client_secret = "your-client-secret"
tenant_id = "your-tenant-id"
subscription_id = "your-subscription-id"

# Create an Azure Container Service client
credentials = ServicePrincipalCredentials(
    client_id=client_id,
    secret=client_secret,
    tenant=tenant_id
)
client = ContainerServiceClient(credentials, subscription_id)

# Get the list of AKS clusters in your subscription
clusters = client.managed_clusters.list()

# Iterate over the clusters
for cluster in clusters:
    # Get the version of Kubernetes that the cluster is running
    version = cluster.kubernetes_version
    print(f"Cluster {cluster.name} is running Kubernetes version {version}")

    # Check if there is a newer version of Kubernetes available
    response = requests.get("https://azure.github.io/AKS/kubernetes_version_list.json")
    versions_json = json.loads(response.text)
    latest_version = versions_json["latest_version"]
    if version != latest_version:
        print(f"  A newer version of Kubernetes is available: {latest_version}")

# This script lists all of the AKS clusters in your subscription, and then checks if there is a newer version of Kubernetes available for each cluster. If a newer version is available, it prints the version number.
#You will need to have the Azure Python SDK (azure-mgmt-containerservice) and the requests library installed and configured on your machine in order to run this script. You can install the Azure Python SDK using pip install azure-mgmt-containerservice, and you can install the requests library using pip install requests. You will also need to have an Azure service principal, which you can obtain by following the instructions in the Azure documentation.
