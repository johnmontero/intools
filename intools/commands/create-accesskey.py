import click
import termtables as tt

from intools.main import pass_context
from intools.utils.iam import create_access_key
from intools.utils.iam import delete_access_key
from intools.utils.iam import list_access_keys
from intools.utils.mail import create_mail_html
from intools.utils.mail import build_msg_to_mail
from intools.utils.mail import send_mail_by_smtp

def send_to_email(ctx, email, data, send_by_ses):
    if email is not None and ctx.config['smtp']['host'].get() is not None:
        email_html = create_mail_html('not-secret-access-key.html', data)
        msg_to_mail = build_msg_to_mail(
            ctx.config['email']['email_from'].get(),
            [email],
            'Notificación de Secret Access Key para su cuenta de AWS',
            email_html
        )

        send_mail_by_smtp(
            ctx.config['smtp']['host'].get(),
            ctx.config['smtp']['port'].get(),
            msg_to_mail,
            ctx.config['smtp']['user'].get() if  send_by_ses else None,
            ctx.config['smtp']['password'].get() if  send_by_ses else None
        )

def force_delete_accesskey(username):
    access_keys = list_access_keys(username)
    if len(access_keys) > 0:
        for access_key in access_keys:
            access_key_id = access_key.get('AccessKeyId')
            response = delete_access_key(username, access_key_id)
            if len(response) > 0:
                if 'HTTPStatusCode' in response:
                    if response.get('HTTPStatusCode') == 200:
                        click.echo(f'Deletion the access key id {access_key_id} was successful')
                    else:
                        click.echo(f'Cannot delete the access key id {access_key_id}')


@click.command()
@click.option('--username', required=True, help='The name of the IAM user that the new key will belong to.')
@click.option('--email', help='The email of the IAM user to send notification.')
@click.option('--force', is_flag=True, default=False, help='Force creation of access key.')
@click.option('--ses', is_flag=True, default=False, help='Send by SES for AWS.')
@pass_context
def command(ctx, **kwargs):
    """Create Access Key for User."""

    # Get values of parameters
    username = kwargs.get('username')
    email = kwargs.get('email')
    force = kwargs.get('force')
    send_by_ses = kwargs.get('ses')

    click.echo()
    if force:
        click.echo(f'Force deletion of access keys for Username: {username}')
        force_delete_accesskey(username)
        click.echo()

    click.echo(f'Create access key for Username: {username}')
    if email is not None:
        click.echo(f'Send notification to email: {email}')
        click.echo()

    access_key = create_access_key(username)

    if len(access_key) > 0:
        header = ["AccessKeyId", "SecretAccessKey", "CreateDate", "Status"]
        data = []
        data.append([
            access_key.get('AccessKeyId'),
            access_key.get('SecretAccessKey'),
            str(access_key.get('CreateDate')),
            access_key.get('Status')
        ])

        # Print List access key
        tt.print(
            data,
            header=header,
            style=tt.styles.ascii_thin_double,
            padding=(0, 1),
            alignment="cccc"
        )

        # Send notification
        send_to_email(ctx, email, access_key, send_by_ses)
    click.echo()