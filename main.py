import smtplib
from email.message import EmailMessage
import ssl

sender = "hi_hamzaoui@esi.dz"
pwd = "fnuaouprnyozevwc"
receiver = "idrissham2000@gmail.com"

subject = "first attempt to send an email with python"
body = """
Salut,

ce mail est un test, supprime moi frerot !!
"""


em = EmailMessage()
em["From"] = sender
em["To"] = receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()


with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(sender, pwd)
    smtp.sendmail(sender, receiver, em.as_string())

