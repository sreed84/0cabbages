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
