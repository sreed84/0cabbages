#Python script that will delete all expired SSL/TLS certificates in your AWS account

import boto3

# Create an ACM client
acm_client = boto3.client('acm')

# List all of the SSL/TLS certificates in your account
certificates = acm_client.list_certificates()

# Iterate through the list of certificates
for certificate in certificates['CertificateSummaryList']:
    # Get the certificate details
    cert_details = acm_client.describe_certificate(CertificateArn=certificate['CertificateArn'])

    # Check if the certificate is expired
    if cert_details['Certificate']['Status'] == 'EXPIRED':
        # Delete the expired certificate
        acm_client.delete_certificate(CertificateArn=certificate['CertificateArn'])
        print(f"Deleted expired certificate {certificate['DomainName']}")
# This script will list all of the SSL/TLS certificates in your AWS account, and then iterate through the list and check if any of the certificates are expired. If a certificate is expired, it will be deleted using the delete_certificate method of the ACM client.
# You can modify this script to fit your specific needs, such as deleting only certain types of certificates or filtering the list of certificates based on their domain name.
