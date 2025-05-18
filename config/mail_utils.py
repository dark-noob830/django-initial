import resend
from django.core.mail import send_mail as django_send_mail
from config.sett1ng.base import *
from django.conf import settings

if deploy :
    resend.api_key = env("RESEND_API_KEY")


def send_mail(subject, body, to_email):
    if deploy :
        params: resend.Emails.SendParams = {
            "from": "info@batbooks.ir",
            "to": to_email,
            "subject": subject,
            "html": f"<p>{body}</p>",
        }

        try:
            resend.Emails.send(params)
        except Exception as e:
            print(f"[Resend error] {e}")

    else:
        django_send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            to_email,
            fail_silently=False,
        )