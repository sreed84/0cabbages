import boto3

# Create an AWS Certificate Manager client
acm = boto3.client("acm")

# List all of the certificates in your AWS account
certificates = acm.list_certificates()

# Iterate over the certificates
for certificate in certificates["CertificateSummaryList"]:
    # Get the certificate details
    details = acm.describe_certificate(CertificateArn=certificate["CertificateArn"])
    # Check if the certificate has expired
    if details["Certificate"]["Status"] == "EXPIRED":
        # Print the ARN of the expired certificate
        print(certificate["CertificateArn"])

        
#This script lists all of the certificates in your AWS account, and then checks the status of each certificate. If the status is "EXPIRED", it prints the ARN of the expired certificate.

#You will need to have the AWS SDK for Python (Boto3) installed and configured on your machine in order to run this script. You can install Boto3 using pip install boto3. You will also need to have an AWS access key and secret key, which you can obtain from the AWS Management Console.
