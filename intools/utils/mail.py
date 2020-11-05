import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

from .render import render_template
from .render import templates_dir

def create_mail_html(name, data):
    context = {'data': data }
    return render_template(templates_dir, name, **context)

def build_msg_to_mail(email_from, emails_to, subject, email_html):

    msg = MIMEMultipart('alternative')
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg['From'] = email_from
    msg['To'] = COMMASPACE.join(emails_to)

    part_text = MIMEText(email_html, 'plain', 'utf-8')
    part_html = MIMEText(email_html, 'html', 'utf-8')
    msg.attach(part_text)
    msg.attach(part_html)

    return msg

def send_mail(host, port, msg):
    smtp_server = smtplib.SMTP(host, port)
    smtp_server.send_message(msg)
    smtp_server.quit()