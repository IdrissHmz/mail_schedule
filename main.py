import smtplib
from email.message import EmailMessage
import ssl


def create_email_message(sender, receivers, subject, body):
    em = EmailMessage()
    em["From"] = sender
    em["To"] = receivers
    em["Subject"] = subject
    em.set_content(body, subtype="html")

    # em.contentmanager.set_content(msg, <'str'>, subtype="plain", charset='utf-8' cte=None, disposition=None, filename=None, cid=None, params=None, headers=None)
    # em.contentmanager.set_content(msg, <'bytes'>, maintype, subtype, cte="base64", disposition=None, filename=None, cid=None, params=None, headers=None)
    # em.contentmanager.set_content(msg, <'EmailMessage'>, cte=None, disposition=None, filename=None, cid=None, params=None, headers=None)
    # em.contentmanager.set_content(msg, <'list'>, subtype='mixed', disposition=None, filename=None, cid=None, params=None, headers=None)
    return em


def send(sender, receiver, em):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(sender, pwd)
        smtp.sendmail(sender, receiver, em.as_string())


def add_attachment(pdf, em):
    with open(pdf, "rb") as file:
        em.add_attachment(
            file.read(),
            maintype="application",
            subtype="octet-stream",
            filename=file.name,
        )


sender = "hi_hamzaoui@esi.dz"
pwd = "fnuaouprnyozevwc"
receivers = "idrissham2000@gmail.com"

subject = "first attempt to send an email with python"
body = """
<!DOCTYPE html>
<html>

<head>
    <title></title>
    <link href="https://svc.webspellchecker.net/spellcheck31/lf/scayt3/ckscayt/css/wsc.css" rel="stylesheet"
        type="text/css" />
</head>

<body><span
        style="background-color:rgb(255, 255, 255); color:rgb(34, 34, 34); font-family:arial,helvetica,sans-serif; font-size:small">Bonjour
        Monsieur.</span><br />
    <span
        style="background-color:rgb(255, 255, 255); color:rgb(34, 34, 34); font-family:arial,helvetica,sans-serif; font-size:small">J&#39;esp&egrave;re
        que ce mail vous trouvera en bonne sant&eacute;!</span><br />
    <br />
    <span
        style="background-color:rgb(255, 255, 255); color:rgb(34, 34, 34); font-family:arial,helvetica,sans-serif; font-size:small">Je
        suis actuellement &eacute;tudiant en 5&eacute;me &agrave; l&#39;Ecole Sup&eacute;rieure d&#39;Informatique
        d&#39;Alger (ESI ex INI) et je suis a la recherche d&#39;un theme pour mener mon projet de fin
        d&#39;&eacute;tudes et en consultant les travaux men&eacute;s par le laboratoire LORIA et ses &eacute;quipes,
        les axes de recherches de cet institut me tentent et m&#39;int&eacute;ressent beaucoup.</span><br />
    <br />
    <span
        style="background-color:rgb(255, 255, 255); color:rgb(34, 34, 34); font-family:arial,helvetica,sans-serif; font-size:small">Je
        vous &eacute;cris ce mail pour vous demander de me proposer un sujet de PFE au niveau de votre institut si
        possible.</span><br />
    <br />
    <span
        style="background-color:rgb(255, 255, 255); color:rgb(34, 34, 34); font-family:arial,helvetica,sans-serif; font-size:small">je
        vous joins en fichier attach&eacute; le dossier qui contient mes relev&eacute;s de note, mon CV et ma lettre de
        motivation, ainsi que mes certifications et attestations de compl&eacute;tion de cours. De plus, voici mon lien
        GitHub pour voir quelques uns de mes travaux :&nbsp;</span><a href="https://github.com/IdrissHmz"
        target="_blank">https://github.com/IdrissHmz</a><br />
    <br />
    <span
        style="background-color:rgb(255, 255, 255); color:rgb(34, 34, 34); font-family:arial,helvetica,sans-serif; font-size:small">Cordialement</span>
</body>

</html>
"""

with open("html_formatted_emails/example.html", "rb") as html:
    body = str(html.read())
    body = body.replace("\n", "")
    # body = """
    # """


em = create_email_message(sender, receivers, subject, body)
send(sender, receivers, em)
