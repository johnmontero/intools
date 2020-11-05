import click
import boto3
import botocore

iam = boto3.client('iam')

def create_access_key(username):
    response = {}
    try:
        response = iam.create_access_key(UserName=username)
    except botocore.exceptions.ClientError as error:
        if error.response['Error']['Code'] == 'LimitExceededException':
            click.echo('API call limit exceeded; backing off and retrying...')
        else:
            click.echo(error)

    return response['AccessKey'] if 'AccessKey' in  sorted(response) else {}

def list_access_keys(username):
    response = {}
    try:
        response = iam.list_access_keys(UserName=username)
    except botocore.exceptions.ClientError as error:
        if error.response['Error']['Code'] == 'ServiceFailureException':
            click.echo('Error ServiceFailureException, please retrying...')
        else:
            click.echo(error)

    return response['AccessKeyMetadata'] if 'AccessKeyMetadata' in  sorted(response) else {}

def delete_access_key(username, access_key_id):
    response = {}
    try:
        response = iam.delete_access_key(UserName=username, AccessKeyId=access_key_id)
    except botocore.exceptions.ClientError as error:
        if error.response['Error']['Code'] == 'LimitExceededException':
            click.echo('API call limit exceeded; backing off and retrying...')
        else:
            click.echo(error)

    return response['ResponseMetadata'] if 'ResponseMetadata' in  sorted(response) else {}
