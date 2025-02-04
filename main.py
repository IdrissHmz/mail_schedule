import smtplib
from email.message import EmailMessage
import ssl
import json


def create_email_message(sender, receivers, subject, body):
    em = EmailMessage()
    em["From"] = sender
    em["To"] = receivers
    em["Subject"] = subject
    em.set_content(body, subtype="html")
    return em


def send(sender, receiver, em):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(sender, APP_PASSWORD)
        smtp.sendmail(sender, receiver, em.as_string())


def add_attachment(pdf, em):
    with open(pdf, "rb") as file:
        em.add_attachment(
            file.read(),
            maintype="application",
            subtype="octet-stream",
            filename=file.name,
        )

def create_body(args, type):
    body = ''
    match type :
        case 'stage_fr':
            with open("html_formatted_emails/stage_fr.html", "rb") as html:
                body = html.read().decode("utf-8")
                body = body.format(laboratoire=args['laboratoire'], github=args['github']).replace(
                    "\n", ""
                )
        case 'master_en':
            with open("html_formatted_emails/master_en.html", "rb") as html:
                body = html.read().decode("utf-8")
                body = body.replace(
                    "\n", ""
                )
        case 'job':
            print('job')        
        case _:
            print('no type')   
    return body  

sender = "hi_hamzaoui@esi.dz"
APP_PASSWORD = "fnuaouprnyozevwc"
type = 'stage_fr'

 
conf = json.load(open('conf.json'))
var = conf[type]
sender = var['sender']
receivers = var['receivers']
subject = var['subject']
args_body = var['args_body']


body = create_body(args_body, type)
em = create_email_message(sender, receivers, subject, body)
send(sender, receivers, em)
