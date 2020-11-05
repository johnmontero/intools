import click
import termtables as tt

from intools.main import pass_context
from intools.utils.iam import list_access_keys

@click.command()
@click.option('--username', required=True, help='The name of the user to list accces keys')
@pass_context
def command(ctx, **kwargs):
    """List Access Keys for User."""
    
    # Get values of parameters
    username = kwargs.get('username')

    click.echo()
    click.echo(f'List access keys for Username: {username}')
    click.echo()
    
    access_keys = list_access_keys(username)

    if len(access_keys) > 0:
        header = ["AccessKeyId", "CreateDate", "Status"]
        data = []
        for access_key in access_keys:
            data.append([
                access_key.get('AccessKeyId'),
                str(access_key.get('CreateDate')),
                access_key.get('Status')
            ])

        # Print List access keys
        tt.print(
            data,
            header=header,
            style=tt.styles.ascii_thin_double,
            padding=(0, 1),
            alignment="ccc"
        )

    click.echo()