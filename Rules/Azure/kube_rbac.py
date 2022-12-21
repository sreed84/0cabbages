# Python script that will check if RBAC is enabled for an AKS cluster

import os

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.containerservice import ContainerServiceClient
from kubernetes import client, config

# Set the AKS resource group and cluster name
RESOURCE_GROUP_NAME = 'my-resource-group'
CLUSTER_NAME = 'my-cluster'

# Set your Azure Active Directory (AAD) tenant ID and client ID
TENANT_ID = 'your-tenant-id'
CLIENT_ID = 'your-client-id'
CLIENT_SECRET = 'your-client-secret'

# Create a Service Principal credentials object
credentials = ServicePrincipalCredentials(
    client_id=CLIENT_ID,
    secret=CLIENT_SECRET,
    tenant=TENANT_ID
)

# Create a Container Service client
client = ContainerServiceClient(credentials, subscription_id=os.environ['AZURE_SUBSCRIPTION_ID'])

# Get the AKS cluster
cluster = client.managed_clusters.get(RESOURCE_GROUP_NAME, CLUSTER_NAME)

# Get the AKS cluster's API server URL and certificate authority data
api_server_url = cluster.fqdn
ca_data = cluster.certificate_profile.ca_certificate

# Create a Kubernetes Configuration object using the API server URL and certificate authority data
configuration = client.Configuration()
configuration.host = api_server_url
configuration.ssl_ca_cert = ca_data

# Create a Kubernetes API client using the Configuration object
api_client = client.ApiClient(configuration)

# Check if RBAC is enabled
rbac_enabled = api_client.call_api('/apis/rbac.authorization.k8s.io', 'get',
                                   _preload_content=False).status == 200

if rbac_enabled:
    print("RBAC is enabled for AKS cluster '{CLUSTER_NAME}'")
else:
    print("RBAC is not enabled for AKS cluster '{CLUSTER_NAME}'")

# This script will get the API server URL and certificate authority data for the AKS cluster using the managed_clusters client, and then use these values to create a Kubernetes Configuration object. It will then create a Kubernetes API client using the Configuration object, and make a request to the /apis/rbac.authorization.k8s.io endpoint to check if RBAC is enabled. If the request returns a status code of 200, RBAC is enabled; otherwise, it is not enabled.
# You can modify this script to fit your specific needs, such as checking multiple AKS clusters or printing a custom message depending on the RBAC status.
