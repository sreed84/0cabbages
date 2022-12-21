# Python script to enable and configure RBAC for an Azure Kubernetes Service (AKS) cluster

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

# Enable RBAC
rbac_api = client.RbacAuthorizationV1Api(api_client)
rbac_api.create_cluster_role_binding(client.V1ClusterRoleBinding(
    metadata=client.V1ObjectMeta(name='cluster-admin'),
    role_ref=client.V1RoleRef(api_group='rbac.authorization.k8s.io', kind='ClusterRole', name='cluster-admin'),
    subjects=[client.V1Subject(api_group='rbac.authorization.k8s.io', kind='User', name='system:serviceaccount:kube-system:default')]
))

print("Successfully enabled and configured RBAC for AKS cluster '{CLUSTER_NAME}'")


# This script will get the API server URL and certificate authority data for the AKS cluster using the managed_clusters client, and then use these values to create a Kubernetes Configuration object. It will then create a Kubernetes API client using the Configuration object, and create a V1ClusterRoleBinding object to enable RBAC. Finally, it will use the create_cluster_role_binding method of the RbacAuthorizationV1Api client to create the cluster role binding and enable RBAC.

