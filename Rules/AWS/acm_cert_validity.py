import boto3

client = boto3.client("acm")

paginator = client.get_paginator("list_certificates")

certificates = []
for page in paginator.paginate():
    certificates.extend(page["CertificateSummaryList"])

not_validated = [cert for cert in certificates if cert["Status"] != "ISSUED"]

if not_validated:
    print("There are certificates that are not validated:")
    for cert in not_validated:
        print(f"- {cert['DomainName']} ({cert['Status']})")
else:
    print("All certificates are validated.")
