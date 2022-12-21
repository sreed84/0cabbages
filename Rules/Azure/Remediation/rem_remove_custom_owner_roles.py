# Python script that will delete all custom owner roles that do not comply with a set of compliance rules
# To remove all non-compliant custom owner roles from your Microsoft Azure cloud account, you can use the Azure Python SDK (azure-mgmt-authorization).

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

# List all of the custom owner roles in the Azure account
roles = client.role_definitions.list(
    filter="roleName eq 'Owner' and not startswith(id, 'BA92C095-5D5A-4F66-9CCF-')"
)

# Delete each role that does not comply with the compliance rules
for role in roles:
    print(f"Deleting role '{role.name}' ({role.id})")
    client.role_definitions.delete(role.id)
# This script will create an Authorization Management client using the Service Principal credentials object, and use the list method of the role_definitions client to get a list of all custom owner roles in the Azure account that do not comply with a set of compliance rules (specified by the filter parameter). It will then iterate through the list of roles and use the delete method of the role_definitions client to delete each non-compliant role.
# You can modify this script to fit your specific needs, such as specifying different compliance rules or deleting roles with a different permission level.
