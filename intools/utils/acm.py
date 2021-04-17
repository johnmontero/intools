import click
import boto3
import botocore

def describe_certificate(region_name, certificate_arn):
    response = {}
    try:
        acm = boto3.client('acm', region_name=region_name)
        response = acm.describe_certificate(
            CertificateArn=certificate_arn
        )
    except botocore.exceptions.ClientError as error:
        if error.response['Error']['Code'] == 'ServiceFailureException':
            click.echo('Error ServiceFailureException, please retrying...')
        else:
            click.echo(error)

    return response['Certificate'] if 'Certificate' in  sorted(response) else {}

def list_certificates(region_name):
    response = {}
    try:
        acm = boto3.client('acm', region_name=region_name)
        response = acm.list_certificates(
            CertificateStatuses=['ISSUED']
        )
    except botocore.exceptions.ClientError as error:
        if error.response['Error']['Code'] == 'ServiceFailureException':
            click.echo('Error ServiceFailureException, please retrying...')
        else:
            click.echo(error)

    return response['CertificateSummaryList'] if 'CertificateSummaryList' in  sorted(response) else {}