# To create a custom role in Microsoft Azure using Python, you will need to use the Azure Resource Manager Python library and the Azure Management Libraries for Python.

from azure.mgmt.authorization import AuthorizationManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource.resources.models import ResourceGroup
from azure.common.credentials import ServicePrincipalCredentials

# create a function to create the custom role. This function should take a subscription ID, resource group name, and role name as arguments, and return the created role

def create_custom_role(subscription_id, resource_group_name, role_name):
    # Create the clients
    credentials = ServicePrincipalCredentials(
        client_id=CLIENT_ID,
        secret=CLIENT_SECRET,
        tenant=TENANT_ID
    )
    auth_client = AuthorizationManagementClient(credentials, subscription_id)
    resource_client = ResourceManagementClient(credentials, subscription_id)

    # Create the resource group if it doesn't exist
    resource_group = ResourceGroup(location='eastus')
    resource_client.resource_groups.create_or_update(resource_group_name, resource_group)

    # Define the permissions and actions for the custom role
    actions = [
        "Microsoft.Authorization/*/Write",
        "Microsoft.Authorization/*/Delete"
    ]
    not_actions = []
    role_definition = {
        "Name": role_name,
        "IsCustom": True,
        "Description": "This role allows the user to manage resource locks in the Azure subscription.",
        "Actions": actions,
        "NotActions": not_actions,
        "AssignableScopes": [f'/subscriptions/{subscription_id}']
    }

    # Create the custom role
    role_definition = auth_client.role_definitions.create_or_update(
        resource_group_name,
        role_name,
        role_definition
    )
    return role_definition
# To use this function, you can call it with the desired subscription ID, resource group name, and role name as arguments

subscription_id = 'SUBSCRIPTION_ID'
resource_group_name = 'RESOURCE_GROUP_NAME'
role_name = 'Custom Lock Management Role'

role = create_custom_role(subscription_id, resource_group_name, role_name)
print(f'Custom role created: {role.name}')

# This will create a custom role with the specified name and permissions in your Azure subscription.
