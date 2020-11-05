import click

from intools.main import pass_context
from intools.utils.iam import delete_access_key

@click.command()
@click.option('--username', required=True, help='The name of the user whose access key pair you want to delete.')
@click.option('--access-key-id', required=True, help='The access key ID you want to delete.')
@pass_context
def command(ctx, **kwargs):
    """Delete Access Key for User."""
    
    # Get values of parameters
    username = kwargs.get('username')
    access_key_id = kwargs.get('access_key_id')

    click.echo()
    click.echo(f'Delete access key for Username: {username}')
    click.echo(f'Access key ID: {access_key_id}')
    click.echo()
    
    response = delete_access_key(username, access_key_id)

    if len(response) > 0:
        if 'HTTPStatusCode' in response:
            if response.get('HTTPStatusCode') == 200:
                click.echo('Deletion the access key was successful')
            else:
                click.echo('Cannot delete the access key')

    click.echo()