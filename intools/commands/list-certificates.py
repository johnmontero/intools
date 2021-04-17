import click
import termtables as tt

from intools.main import pass_context
from intools.utils.acm import list_certificates
from intools.utils.acm import describe_certificate

@click.command()
@click.option('--region', required=True, help='The name of region to list certificates')
@click.option('--exclude-domain', multiple=True, help='The domain name to exclude')
@pass_context
def command(ctx, **kwargs):
    """List Certificates for Region."""
    
    # Get values of parameters
    region = kwargs.get('region')
    exclude_domains = list(kwargs.get('exclude_domain'))

    click.echo()
    click.echo(f'List certificates for Region: {region}')
    if len(exclude_domains) > 0:
        domains = ", ".join(exclude_domains)
        click.echo(f'Exclude domains: {domains}')
    click.echo()
    
    certificates = list_certificates(region)

    if len(certificates) > 0:
        header = [
            "CertificateArn",
            "DomainName",
            "NotAfter"
        ]
        data = []
        for certificate in certificates:
            include_domain = True
            domain_name = certificate.get('DomainName')

            if len(exclude_domains) > 0:
                for exclude_domain in exclude_domains:
                    if domain_name.find(exclude_domain) != -1:
                        include_domain = False
                        break

            if include_domain:
                certificate_arn = certificate.get('CertificateArn')
                response = describe_certificate(region, certificate_arn)
                subject_alternative_names = ", ".join(response["SubjectAlternativeNames"])
                not_after = response["NotAfter"]

                click.echo(f'DomainName             : {domain_name}')
                click.echo(f'SubjectAlternativeNames: {subject_alternative_names}')
                click.echo(f'NotAfter               : {not_after}')
                click.echo(f'CertificateArn         : {certificate_arn}')
                click.echo()

    click.echo()