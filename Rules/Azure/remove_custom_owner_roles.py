# Python script that will list all of the owner roles in your Azure account

import os

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.authorization import AuthorizationManagementClient

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

# Create an Authorization Management client
client = AuthorizationManagementClient(credentials, subscription_id=os.environ['AZURE_SUBSCRIPTION_ID'])

# List all of the owner roles in the Azure account
roles = client.role_definitions.list(filter="roleName eq 'Owner'")

# Print the role names and descriptions
for role in roles:
    print(f"Name: {role.name}")
    print(f"Description: {role.description}")
    print()

# This script will create an Authorization Management client using the Service Principal credentials object, and use the list method of the role_definitions client to get a list of all of the owner roles in the Azure account. It will then iterate through the list of roles and print the role names and descriptions.
# You can modify this script to fit your specific needs, such as filtering the list of roles based on a different role name or checking for custom roles with a different permission level.
