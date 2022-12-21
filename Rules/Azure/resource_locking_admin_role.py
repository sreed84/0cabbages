# Python script that will list all of the custom roles in each Azure subscription and check if any of them have the "Microsoft.Authorization/locks/write" action assigned
# To determine if there is a custom role assigned to manage resource locking within each Azure subscription, you can use the Azure Python SDK (azure-mgmt-authorization)

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

# Get a list of all Azure subscriptions
subscriptions = client.subscriptions.list()

# Iterate through each subscription
for subscription in subscriptions:
    # Get the subscription ID
    subscription_id = subscription.subscription_id

    # Set the subscription ID for the Authorization Management client
    client.config.subscription_id = subscription_id

    # List all of the custom roles in the subscription
    roles = client.role_definitions.list(filter="roleType eq 'CustomRole'")

    # Check if any of the roles have the "Microsoft.Authorization/locks/write" action assigned
    for role in roles:
        for action in role.permissions:
            if action.actions[0] == "Microsoft.Authorization/locks/write":
                print(f"Custom role '{role.name}' has 'Microsoft.Authorization/locks/write' action assigned in subscription '{subscription_id}'")

# This script will create an Authorization Management client using the Service Principal credentials object, and use the list method of the subscriptions client to get a list of all Azure subscriptions. It will then iterate through each subscription, set the subscription ID for the client, and use the list method of the role_definitions client to get a list of all custom roles in the subscription. Finally, it will iterate through each role and check if the "Microsoft.Authorization/locks/write" action is assigned to the role. If it is, it will print the role name and subscription ID.
# You can modify this script to fit your specific needs, such as checking for a different action or checking for roles with a different permission level.
